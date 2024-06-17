def text_reverse(new_string: str) -> str:
    """Переворачивает строку"""
    return new_string[::-1]


def up_first(sentence: str) -> str:
    """Делает первую букву строки заглавной"""
    if sentence:
        return sentence[0].upper() + sentence[1:]
    else:
        return sentence
