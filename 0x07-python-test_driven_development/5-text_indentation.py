#!/usr/bin/python3
"""text indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: . ? :

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If the input is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    new_text = ""

    text_len = len(text)
    for i in range(text_len):
        if text[i] == ' ':
            if new_text == "" or new_text[-1] == "\n":
                continue
            new_text += text[i]
        elif text[i] in chars:
            new_text += text[i] + "\n\n"
        else:
            new_text += text[i]
    print(new_text, end="")
