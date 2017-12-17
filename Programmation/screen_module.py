"""
This module is in charge of the user interface, i.e. it shows the right text in the chosen language.
"""

# TODO: COMMENT CODE!!!


import screen_constants


def show_start_ask_language():
    """
    asks the language the user wants to use at the beginning:french or english
    :return:
    """
    return input(START_ASK_LANGUAGE)


def show_language_settings():
    """

    :return:
    """
    return input(LANGUAGE_SETTINGS)


def show_main_menu(english):
    """

    :param english:
    :return:
    """
    if english:
        return input(ENGLISH_MAIN_MENU)
    elif english == False:
        return input(FRENCH_MAIN_MENU)
    else:
        return "this should never happen"


def show_principles(english, encrypting):
    """

    :param english:
    :param encrypting:
    :return:
    """
    if english:
        if encrypting:
            return input(ENGLISH_PRINCIPLES_ENCRYPTING)
        if encrypting == false:
            return input(ENGLISH_PRINCIPLES_DECRYPTING)
    elif english == False:
        if encrypting:
            return input(NGLISH_PRINCIPLES_ENCRYPTING)
        if encrypting == false:
            return input(ENGLISH_PRINCIPLES_DECRYPTING)
    else:
        return "this should never happen"


def show_ask_key(english):
    """

    :param english:
    :return:
    """
    if english:
        if caesar:
            return input(ENGLISH_ASK_KEY_CAESAR)
        elif vigenere:
            return input(ENGLISH_ASK_KEY_VIGENERE)
        elif enigma:
            return input(ENGLISH_ASK_KEY_ENIGMA)
        else:
            return "this should never happen"
    elif english == False:
        if caesar:
            return input(FRENCH_ASK_KEY_CAESAR)
        elif vigenere:
            return input(FRENCH_ASK_KEY_VIGENERE)
        elif enigma:
            return input(FRENCH_ASK_KEY_ENIGMA)
        else:
            return "this should never happen"


def show_ask_text(english):
    """

    :param english:
    :return:
    """
    if english:
        return input(ENGLISH_ASK_TEXT)
    elif english == False:
        return input(FRENCH_ASK_TEXT)
    else:
        return "this should never happen"


def show_treated_text(english, encrypting):
    """

    :param english:
    :param encrypting:
    :return:
    """
    if english:
        if encrypting:
            print(ENGLISH_ENCRYPTED_TEXT)
        elif encrypting == False:
            print(ENGLISH_DECRYPTED_TEXT)
    if english == False:
        if encrypting:
            print(FRENCH_ENCRYPTED_TEXT)
        elif encrypting == False:
            print(FRENCH_DECRYPTED_TEXT)


def show_help_principles(english):
    """

    :param english:
    :return:
    """
    if english:
        print(ENGLISH_HELP_PRINCIPLES)
    else:
        print(FRENCH_HELP_PRINCIPLES)


def show_quit_message(english):
    """

    :param english:
    :return:
    """
    if english:
        print(ENGLISH_QUIT_MESSAGE)
    else:
        print(FRENCH_QUIT_MESSAGE)

