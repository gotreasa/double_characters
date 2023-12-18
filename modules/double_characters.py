def double_chars(string: str) -> str:
    if not isinstance(string, str):
        raise ValueError("❗️ Input should be a string")

    result = ""
    for letter in string:
        result += letter * 2

    return result
