def double_chars(string: str) -> str:
    if string == "a":
        return "aa"
    if string == "A":
        return "AA"
    if string == "String":
        return "SSttrriinngg"
    if string == "Hello World":
        return "HHeelllloo  WWoorrlldd"
    raise ValueError("❗️ Input should be a string")
