from typing import List


def do_a_barrel_roll(numbers: List[int], k: int) -> List[int]:
    n = len(numbers)
    if n == 0 or k == 0:
        return numbers
    k %= n
    return numbers[k:] + numbers[:k]
