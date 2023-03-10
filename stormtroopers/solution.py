from typing import List

def stormtroopers(numbers: List[int]) -> List[int]:

    x = [] 
    dictionnaire = {}

    for i in numbers:
        if i in dictionnaire:
           dictionnaire[i] +=1 
        else:
            dictionnaire[i] = 1

    return [key for key, value in dictionnaire.items() if value == 1]




