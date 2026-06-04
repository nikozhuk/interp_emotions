# temporal.py — temporal concept prompts for SAE geometry analysis
# Design: 5 categories × 20 prompts. First 5 in each category are minimal pairs
# across the same anchor scenarios. Remaining 15 vary content broadly.

# === MINIMAL PAIR ANCHORS (same content, varied tense) ===
# A: walked to the store
# B: finished the report
# C: arrived in Berlin
# D: sent the contract
# E: read the book

PAST_PROMPTS = [
    # Minimal pairs (5)
    "Yesterday, she walked to the store.",
    "He finished the report last week.",
    "The team arrived in Berlin on Monday.",
    "She sent the contract two days ago.",
    "He read the book during the summer.",
    # Varied content with -ed morphology (5)
    "The factory closed in 1987.",
    "They danced until midnight at the wedding.",
    "The negotiations ended without a deal.",
    "She painted the entire kitchen over the weekend.",
    "The army retreated after the third assault.",
    # Varied content with temporal adverbs, mixed morphology (5)
    "Long ago, the river ran much wider.",
    "An hour earlier, he had been on a phone call.",
    "Decades before, the harbor had been a fishing village.",
    "Three years prior, she lived in Lisbon.",
    "Before the war, the family owned a bakery.",
    # Varied content, irregular verbs (5)
    "The glass broke when it hit the floor.",
    "She took the train to Hamburg.",
    "The package came in the afternoon mail.",
    "He spoke quietly during the entire meeting.",
    "The deal fell apart at the last minute.",
]

PRESENT_PROMPTS = [
    # Minimal pairs (5) — present habitual / ongoing
    "She walks to the store every morning.",
    "He finishes the report before each meeting.",
    "The team arrives in Berlin on Mondays.",
    "She sends the contract to every new client.",
    "He reads the book to his daughter each night.",
    # Habitual present (5)
    "The bakery opens at six on weekdays.",
    "He commutes by bike whenever the weather allows.",
    "The committee meets twice a month.",
    "She drinks coffee only in the morning.",
    "The river floods every spring.",
    # Ongoing present-progressive (5)
    "She is reviewing the document right now.",
    "The lecture is currently in progress.",
    "He is sitting at his desk, typing quietly.",
    "The negotiations are continuing into the evening.",
    "The children are playing in the garden.",
    # Stative present (5)
    "The library stands at the corner of the square.",
    "The lake lies just beyond the ridge.",
    "She knows three languages fluently.",
    "The treaty remains in effect until 2030.",
    "He owns a small bookstore in the old town.",
]

FUTURE_PROMPTS = [
    # Minimal pairs (5) — "will" form
    "Tomorrow, she will walk to the store.",
    "He will finish the report by Friday.",
    "The team will arrive in Berlin next week.",
    "She will send the contract by the deadline.",
    "He will read the book on the flight.",
    # "going to" future (5)
    "She is going to apply for the position.",
    "They are going to repaint the office next month.",
    "The festival is going to open on the first of June.",
    "He is going to retire at the end of the year.",
    "The company is going to announce the merger soon.",
    # Present-progressive for near future (5)
    "She is leaving for Paris tomorrow morning.",
    "The chancellor is meeting with the cabinet on Tuesday.",
    "He is starting the new job in September.",
    "We are flying to Hamburg next weekend.",
    "The exhibition is opening on Thursday evening.",
    # Simple present for scheduled future (5)
    "The train arrives at noon.",
    "The conference begins on the fifteenth.",
    "Her flight lands at seven in the morning.",
    "The deadline falls on a Sunday this year.",
    "The new edition appears in stores next month.",
]

COUNTERFACTUAL_PROMPTS = [
    # Minimal pairs (5) — past contrary-to-fact
    "She would have walked to the store, but it was raining.",
    "He would have finished the report, if the system hadn't crashed.",
    "The team would have arrived in Berlin earlier, but the flight was delayed.",
    "She would have sent the contract, if she had received the changes in time.",
    "He would have read the book, but he fell asleep too quickly.",
    # Varied counterfactual past (5)
    "If she had taken the earlier train, she would have made the meeting.",
    "Had the alarm gone off, he wouldn't have missed his flight.",
    "If they had invested in 2010, they would be wealthy now.",
    "She wouldn't have made the mistake, had she read the instructions.",
    "If the bridge hadn't collapsed, the city would have grown faster.",
    # Counterfactual with regret/desire framing (5)
    "He wishes he had studied medicine instead of law.",
    "She regrets that she didn't accept the offer in Munich.",
    "If only they had told her the truth from the start.",
    "He often imagines what life would have been like in Vienna.",
    "She still thinks about the path she didn't take after graduation.",
    # Counterfactual without explicit "if" (5)
    "Born a century earlier, she would have been a court physicist.",
    "Without the war, the city would still have its old library.",
    "A different vote, and the law would have passed.",
    "Given more time, the project would have succeeded.",
    "But for the storm, the harvest would have been excellent.",
]

HYPOTHETICAL_PROMPTS = [
    # Minimal pairs (5) — present/future conditional
    "If she walked to the store, she would feel better.",
    "If he finished the report early, he could leave by three.",
    "If the team arrived in Berlin tonight, they could meet the minister tomorrow.",
    "If she sent the contract today, the deal would close this week.",
    "If he read the book carefully, he would understand the argument.",
    # Open future hypotheticals (5)
    "Should the weather hold, the ceremony will take place outdoors.",
    "In the event of a delay, passengers will receive a refund.",
    "If the data confirms the hypothesis, we can publish next month.",
    "Suppose the merger goes through; the share price would rise sharply.",
    "If demand continues, the factory may add a second shift.",
    # Subjunctive / unreal present (5)
    "If she were the manager, she would restructure the team.",
    "Were he in charge, the policy would be different.",
    "If I were you, I would not sign that contract yet.",
    "If the city had a metro system, traffic would be far lighter.",
    "Were the laws stricter, the river would not be so polluted.",
    # Abstract / philosophical hypotheticals (5)
    "Imagine a world in which gravity were twice as strong.",
    "Consider what would happen if light traveled more slowly.",
    "Suppose every citizen were entitled to a basic income.",
    "What if memory could be transferred between people?",
    "In a society without money, exchange would take other forms.",
]

NEUTRAL_TIMELESS_PROMPTS = [
    # Mathematical / logical
    "The sum of the angles of a triangle equals one hundred eighty degrees.",
    "Seven is a prime number.",
    "Any integer is either even or odd.",
    "The square root of sixteen is four.",
    "Parallel lines never intersect in Euclidean geometry.",
    # Physical / chemical
    "Water boils at one hundred degrees Celsius at standard pressure.",
    "Hydrogen is the lightest element.",
    "Light travels faster than sound.",
    "Iron rusts in the presence of oxygen and moisture.",
    "Magnets attract iron and certain other metals.",
    # Definitional / categorical
    "A triangle has three sides.",
    "Whales are mammals, not fish.",
    "The capital of France is Paris.",
    "Gold is denser than aluminum.",
    "Chess is played on a board of sixty-four squares.",
    # Mathematical relations
    "Multiplication distributes over addition.",
    "Every continuous function on a closed interval attains its maximum.",
    "The determinant of a product equals the product of determinants.",
    "A prime number greater than two is odd.",
    "The exponential function is its own derivative.",
]

ALL_TEMPORAL_CATEGORIES = {
    "past":           PAST_PROMPTS,
    "present":        PRESENT_PROMPTS,
    "future":         FUTURE_PROMPTS,
    "counterfactual": COUNTERFACTUAL_PROMPTS,
    "hypothetical":   HYPOTHETICAL_PROMPTS,
    "neutral":        NEUTRAL_TIMELESS_PROMPTS,
}