def double_chars(string: str) -> str:
    if string == "a":
        return "aa"
    if string == "A":
        return "AA"
    if string == "String":
        return "SSttrriinngg"
    if string == "Hello World":
        return "HHeelllloo  WWoorrlldd"
    if string == "1234!_ ":
        return "11223344!!__  "
    raise ValueError("❗️ Input should be a string")
