def firstNonRepeatingCharacter(string: str) -> int:
    if not len(string):
        return -1
    
    x = {}

    for idx, c in enumerate(string):
        if c not in x:
            x[c] = idx
        else:
            x[c] = len(string)
    
    return -1 if min(x.values()) == len(string) else min(x.values())
