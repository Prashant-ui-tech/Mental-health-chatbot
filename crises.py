from typing import Dict

HIGH_RISK = [
    "kill myself",
    "suicide",
    "end my life",
    "i want to die",
    "i will die",
    "better off dead",
    "overdose",
    "taking pills to die",
    "drink poison"
]

MEDIUM_RISK = [
    "i don't want to live",
    "life is meaningless",
    "no reason to live",
    "i give up",
    "can't go on",
    "want to disappear",
    "self-harm",
    "cutting",
    "starving myself",
    "not eating"
]

LOW_RISK = [
    "feeling sad",
    "depressed",
    "lonely",
    "hopeless",
    "mental breakdown",
    "can't cope",
    "i hate myself"
]

SAFETY_MESSAGE = """
Hey, I hear you, and I want you to know you’re not alone.

Things may feel really heavy right now, but your life is very important.

Please try to reach out to someone you trust — your mom, dad, a close friend, or a professional like a psychologist or counselor.

You don’t have to face this alone. There are people who care about you and want to help.

You matter ❤️
"""

def detect_crisis(text: str) -> Dict:
    text = text.lower()

    for phrase in HIGH_RISK:
        if phrase in text:
            return {"is_crisis": True, "level": "HIGH"}

    for phrase in MEDIUM_RISK:
        if phrase in text:
            return {"is_crisis": True, "level": "MEDIUM"}

    for phrase in LOW_RISK:
        if phrase in text:
            return {"is_crisis": True, "level": "LOW"}

    return {"is_crisis": False, "level": None}



def contains_crisis_keywords(text: str) -> bool:
    return detect_crisis(text)["is_crisis"]