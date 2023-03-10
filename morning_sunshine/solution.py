from typing import List

def morning_sunshine(numbers: List[int]) -> List[int]:
    result = []
    max_value = float("-inf")
    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] > max_value:
            result.append(numbers[i])
            max_value = numbers[i]
    return result[::-1]
