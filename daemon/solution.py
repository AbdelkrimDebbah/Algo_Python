from typing import List

def daemon(numbers: List[int], k: int) -> bool:
    if k < 0 or k > len(numbers):
        return False 

    for i in range(k): 
        if numbers[i] >= numbers[k]:
            return False

    for i in range(k+1,len(numbers)):
        if numbers[i] < numbers[k]:
            return False

    return True