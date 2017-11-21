"""
This module is responsable for the program flow.
"""


# import screen_module
# import text_module


def normalise_letter(x):
    """
    normalisation of the given letter x if it is a special character
    :param: x is the given letter
    :return: chr
    """
    if 'a' <= x <= 'z':
        return x
    elif x in "àâ":
        return 'a'
    elif x in "æ":
        return "ae"
    elif x in "ç":
        return 'c'
    elif x in "èéêë":
        return 'e'
    elif x in "îï":
        return 'i'
    elif x in "ô":
        return 'o'
    elif x in "ùûü":
        return 'u'
    elif x in "ÿ":
        return 'y'
    elif x in "œ":
        return "oe"
    else:
        return "\nSome problem occurred."


def format_text(text):
    """
    formats the given text (deleting numbers, white spaces, etc.)
    :param: text is the text entered by the user which has to be formatted to en-/decrypt it.
    :return: string
    """
    text_list = [x for x in text]
    i = 0
    while i < len(text_list):
        if text_list[i].isalpha():
            # print("***DEBUG*** before normalisation x = ", text_list[i])
            text_list[i] = normalise_letter(text_list[i])
            # print("***DEBUG*** after normalisation x = ", text_list[i])
        else:
            text_list[i] = ''
            # print("***DEBUG*** text = ", text)
        i += 1
    else:
        text = ''.join(text_list)
        text = text.upper()
        return text


def run():
    """
    starts the program
    :return: None
    """
    english = True
    encryption = False
    caesar = False
    vigenere = False
    enigma = False
    key_caesar = 0
    key_vigenere = 'abc'
    key_enigma = 'abc'

    print("***DEBUG*** program is started")
    text = "àâ test1t!? æ test2test,. ç test3test;+ èéêë test4test-% îï t5t$& ô test6test\"/ ùûü t7t{} ÿ t8t[] œ t9t= "
    print("***DEBUG*** test text: ", text)
    print(format_text(text))


run()