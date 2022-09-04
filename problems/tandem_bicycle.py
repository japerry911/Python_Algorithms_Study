from typing import List


def tandemBicycle(
    redShirtSpeeds: List[int], 
    blueShirtSpeeds: List[int], 
    fastest: bool
) -> int:
    total_riders = len(redShirtSpeeds)
    
    redShirtSpeeds.sort(reverse=fastest)
    blueShirtSpeeds.sort(reverse=fastest)
    
    x = []
    
    while len(x) < total_riders:
        r_use = redShirtSpeeds[0]        
        b_use = blueShirtSpeeds[0]

        if r_use >= b_use:
            x.append(r_use)
            redShirtSpeeds.pop(0)
            if not fastest:
                blueShirtSpeeds.pop(0)
        else:
            x.append(b_use)
            blueShirtSpeeds.pop(0)
            if not fastest:
                redShirtSpeeds.pop(0)
    
    return sum(x)
