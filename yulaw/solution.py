from typing import List


def yulaw(s: str) -> str:

    dictionnaire = {}

    for i in s:
        if i in dictionnaire:
           dictionnaire[i] +=1 
        else:
            dictionnaire[i] = 1

    return (''.join((key) for key , value in dictionnaire.items()))
    



