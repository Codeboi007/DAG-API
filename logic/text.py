import random

def augment(text, method):
    words = text.split()

    if method == "synonym":
        replacements = {"quick": "fast", "brown": "dark", "fox": "animal"}
        return " ".join([replacements.get(w, w) for w in words])

    elif method == "deletion":
        if len(words) > 2:
            words.pop(random.randint(0, len(words)-1))
        return " ".join(words)

    return text
