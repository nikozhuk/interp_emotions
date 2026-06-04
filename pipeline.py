"""Reusable SAE feature-extraction pipeline (Gemma-2-2B + GemmaScope).

Single source of truth shared by the joy and temporal notebooks so they
cannot drift apart. Import after the model + SAE are loaded:

    import sys, os, glob
    hit = glob.glob("/kaggle/input/**/pipeline.py", recursive=True)
    sys.path.insert(0, os.path.dirname(hit[0]))
    from pipeline import (init, get_feature_acts, concept_mean,
                          diff_table, decoder_cosines)
    init(model, sae, device)
"""
import torch
import torch.nn.functional as F
import pandas as pd

_MODEL = None
_SAE = None
_DEVICE = None

# Layer-20 / width-16k canonical SAE on Neuronpedia.
NP_URL = "https://neuronpedia.org/gemma-2-2b/20-gemmascope-res-16k/"


def init(model, sae, device):
    """Stash the loaded model / SAE / device for the helpers below."""
    global _MODEL, _SAE, _DEVICE
    _MODEL, _SAE, _DEVICE = model, sae, device


def get_feature_acts(prompt, layer=20):
    """Encode one prompt's residual stream into SAE feature activations.

    The SAE encodes in fp32 — a bf16 encode silently returns all zeros
    (JumpReLU `z > threshold` gate fails everywhere). The `.float()` below
    is load-bearing. Returns (feature_acts, str_tokens).
    """
    tokens = _MODEL.to_tokens(prompt)
    _, cache = _MODEL.run_with_cache(
        tokens,
        names_filter=f"blocks.{layer}.hook_resid_post",
        return_type=None,
    )
    resid = cache[f"blocks.{layer}.hook_resid_post"].squeeze(0).to(_DEVICE).float()
    feature_acts = _SAE.encode(resid)
    return feature_acts, _MODEL.to_str_tokens(prompt)


def concept_mean(prompts, layer=20, agg="last"):
    """Mean feature vector across a prompt set.

    agg="last": last-token activation (default — captures the contextual
                integration of the full sentence, and dodges <bos>).
    agg="mean": mean over tokens EXCLUDING <bos> (acts[1:]); <bos> is an
                attention sink with L0 in the thousands and would swamp it.
    """
    vecs = []
    for p in prompts:
        acts, _ = get_feature_acts(p, layer)
        if agg == "last":
            vecs.append(acts[-1])
        elif agg == "mean":
            vecs.append(acts[1:].mean(0))
        else:
            raise ValueError(f"unknown agg: {agg!r}")
    return torch.stack(vecs).mean(0)


def diff_table(concept_vec, baseline_vec, concept, baseline, k=20):
    """Top-k features by (concept_mean - baseline_mean), with Neuronpedia links.

    Returns a DataFrame: feature_id, diff_score, <concept>_mean,
    <baseline>_mean, neuronpedia.
    """
    diff = concept_vec - baseline_vec
    top = torch.topk(diff, k)
    rows = []
    for score, idx in zip(top.values.tolist(), top.indices.tolist()):
        rows.append({
            "feature_id": idx,
            "diff_score": round(score, 3),
            concept + "_mean": round(concept_vec[idx].item(), 3),
            baseline + "_mean": round(baseline_vec[idx].item(), 3),
            "neuronpedia": NP_URL + str(idx),
        })
    return pd.DataFrame(rows)


def decoder_cosines(feature_ids):
    """Pairwise cosine similarity of features' decoder directions W_dec[i].

    The geometry primitive: are two concepts antipodal (~ -1), orthogonal
    (~ 0), or aligned (~ +1)? Returns a [k, k] tensor on CPU.
    """
    W = _SAE.W_dec[feature_ids].float()
    W = F.normalize(W, dim=1)
    return (W @ W.T).cpu()
