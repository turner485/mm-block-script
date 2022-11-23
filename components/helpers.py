def encode(word: str) -> str:
    """ Encodes each character in a string.
        The word parameter is the whole word/sentence to be encoded.
    """
    encoding_dict = {
        "á": "&aacute;",
        "à": "&agrave;",
        "À": "&Agrave;",
        "ô": "&ocirc;",
        "Ô": "&Ocirc;",
        "Ä": "&Auml;",
        "Ä": "&Auml;",
        "ä": "&auml;",
        "É": "&Eacute;",
        "é": "&eacute;",
        "è": "&egrave;",
        "ê": "&ecirc;",
        "Ö": "&Ouml;",
        "ö": "&ouml;",
        "Ü": "&Uuml;",
        "ü": "&uuml;",
        "ß": "&szlig;",
        "‘": "&lsquo;",
        "’": "&rsquo;",
        "“": "&ldquo;",
        "”": "&rdquo;",
        "€": "&euro;",
        "£": "&pound;",
        "…": "...",
        "–": "&ndash;",
        "•": "&bull;",
        u"\xa0": "&nbsp;",
        u"\0xE1": "",
        "*": '<sup style="line-height: 0; vertical-align: 8px; font-size: 45%">*</sup>',
        "'": '&rsquo;'
    }
    encoded_character_list = []
    if isinstance(word, str):
        word = [str(char).replace(char, encoding_dict.get(char, char)) for char in word]
        word = "".join(word)
        encoded_character_list.append(word)
        return "".join(encoded_character_list)
    else:
        return word