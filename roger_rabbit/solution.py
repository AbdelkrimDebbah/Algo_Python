from typing import List


def roger_rabbit(n: int) -> List[str]:
    
    result = []
    file = ['1']
    
    for n in range(1, n+1):
        premElemFile = file[0]
        file.append(premElemFile + '0')
        file.append(premElemFile + '1')
        
        result.append(file.pop(0))
    return result    
