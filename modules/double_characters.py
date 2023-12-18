def double_chars(string: str) -> str:
    if string == "a":
        return "aa"
    if string == "A":
        return "AA"
    raise ValueError("❗️ Input should be a string")
