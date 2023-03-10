def open_closed(s: str) -> bool:
    count_simple_quote = 0
    count_double_quote = 0
    count_open_bracket = 0
    count_close_bracket = 0
    count_open_parenthesis = 0
    count_close_parenthesis = 0

    for char in s:
        if char == "{" or char == "}":
            return False

        if char == "'":
            count_simple_quote += 1
        elif char == '"':
            count_double_quote += 1
        elif char == "[":
            count_open_bracket += 1
        elif char == "]" and count_open_bracket:
            count_open_bracket -= 1
            if count_open_bracket < 0:
                return False
        elif char == "(":
            count_open_parenthesis += 1
        elif char == ")":
            count_open_parenthesis -= 1
            if count_open_parenthesis < 0:
                return False

    if count_open_bracket != count_close_bracket or count_open_parenthesis != count_close_parenthesis:
        return False

    if (count_close_parenthesis + count_open_parenthesis) % 2 != 0:
        return False

    if (count_close_bracket + count_open_bracket) % 2 != 0:
        return False

    return (count_simple_quote % 2 == 0 and count_double_quote % 2 == 0)