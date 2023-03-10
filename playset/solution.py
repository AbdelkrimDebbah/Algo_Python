def playset(s: str) -> bool:
    
    char_count = {}

    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
        
    return any(count > 1 for count in char_count.values())
