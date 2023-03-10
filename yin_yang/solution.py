def yin_yang(s: str) -> bool:
    stack = []
    count_simple_quote = 0
    count_double_quote = 0

    for char in s:
        if char == "[":
            stack.append("]")
        elif char == "(":
            stack.append(")")
        elif char == "'" and count_simple_quote % 2 == 0:
            stack.append("'")
            count_simple_quote += 1
        elif char == '"' and count_double_quote % 2 == 0:
            stack.append('"')
            count_double_quote += 1
        elif char in ["]", ")", "'", '"']:
            if len(stack) == 0:
                return False
            if char != stack.pop():
                return False
    
    return (len(stack) == 0)