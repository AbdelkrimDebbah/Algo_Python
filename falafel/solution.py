def falafel(s: str) -> bool:
    char_count = [0] * 128
    counter_char_pair = 0

    for char in s:
        char_count[ord(char)] += 1
        if char_count[ord(char)] % 2 == 1:
            counter_char_pair += 1
        else:
            counter_char_pair -= 1

    if counter_char_pair <= 1:
        return True
    else:
        return False
