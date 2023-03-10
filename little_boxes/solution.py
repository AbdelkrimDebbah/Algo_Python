def little_boxes(s: str) -> str:
    return ''.join(sorted(s))

def little_boxes(s: str) -> str:
    array = [0] * 128

    for char in s:
        array[ord(char)] += 1

    result = ''
    for i in range(128):
        result += chr(i) * array[i]

    return result