"""
This module is in charge of the user interface, i.e. it shows the right text in the chosen language.
"""


# TODO: COMMENT CODE!!!


import screen_constants


def show_start_ask_language():
    # TODO add description
    """

    :return:
    """
    chosen_language = input(screen_constants.START_ASK_LANGUAGE)
    return chosen_language


def show_main_menu():
    # TODO add description
    """

    :return:
    """
    if show_start_ask_language() == 'e':
        main_menu = input(screen_constants.ENGLISH_MAIN_MENU)
    elif show_start_ask_language() == 'f':
        main_menu = input(screen_constants.FRENCH_MAIN_MENU)
    return main_menu


def show_principles():
    # TODO add description
    """

    :return:
    """
    # if language chosen is english
    if show_main_menu() == 'c' and show_start_ask_language() == 'e':
        encrypting = input(screen_constants.ENGLISH_PRINCIPLES_ENCRYPTING)
        return encrypting
    elif show_main_menu() == 'd' and show_start_ask_language() == 'e':
        decrypting = input(screen_constants.ENGLISH_PRINCIPLES_DECRYPTING)
        return decrypting
    # if language chosen is french
    elif show_main_menu() == 'c' and show_start_ask_language() == 'f':
        encrypting = input(screen_constants.FRENCH_PRINCIPLES_ENCRYPTING)
        return encrypting
    elif show_main_menu() == 'd' and show_start_ask_language() == 'f':
        decrypting = input(screen_constants.FRENCH_PRINCIPLES_DECRYPTING)
        return decrypting
    elif show_main_menu() == 's':
        language = input(screen_constants.LANGUAGE_SETTINGS)
        return language


# TODO: verify @Fathima as-tu inséré la fonction "show_ask_key" deux fois? :D
# yupp je viens de coriger ça

def show_ask_key():
    # TODO add description
    """

    :return:
    """
    # if language chosen is english
    if show_principles() == 'c' and show_start_ask_language() == 'e':
        key = input(screen_constants.ENGLISH_ASK_KEY_CAESAR)
        return key
    elif show_principles() == 'v' and show_start_ask_language() == 'e':
        key = input(screen_constants.ENGLISH_ASK_KEY_VIGENERE)
        return key
    elif show_principles() == 'e' and show_start_ask_language() == 'e':
        key = input(screen_constants.ENGLISH_ASK_KEY_ENIGMA)
        return key
    elif show_principles() == 'm' and show_start_ask_language() == 'e':
        main_menu = input(screen_constants.ENGLISH_MAIN_MENU)
        return main_menu
    # if language chosen is french
    elif show_principles() == 'c' and show_start_ask_language() == 'f':
        key = input(screen_constants.FRENCH_ASK_KEY_CAESAR)
        return key
    elif show_principles() == 'v' and show_start_ask_language() == 'f':
        key = input(screen_constants.FRENCH_ASK_KEY_VIGENERE)
        return key
    elif show_principles() == 'e' and show_start_ask_language() == 'f':
        key = input(screen_constants.FRENCH_ASK_KEY_ENIGMA)
        return key
    elif show_principles() == 'm' and show_start_ask_language() == 'f':
        main_menu = input(screen_constants.FRENCH_MAIN_MENU)
        return main_menu




def show_ask_text():
    # TODO add description
    """

    :return:
    """
    # if language chosen is english
    if show_start_ask_language() == 'e':
        text = input(screen_constants.ENGLISH_ASK_TEXT)
        if text == 'm':
            return screen_constants.ENGLISH_MAIN_MENU
        else:
            return text
    # if language chosen is french
    elif show_start_ask_language() == 'f':
        text = input(screen_constants.FRENCH_ASK_TEXT)
        if text == 'm':
            return screen_constants.FRENCH_MAIN_MENU
        else:
            return text
    return 0


def show_treated_text():
    # TODO add description
    """

    :return:
    """
    # if language chosen is english
    if show_start_ask_language() == 'e' and show_principles() == "encrypting":
        return screen_constants.ENGLISH_ENCRYPTED_TEXT
    elif show_start_ask_language() == 'e' and show_principles() == "decrypting":
        return screen_constants.ENGLISH_DECRYPTED_TEXT
    # if language chosen is french
    elif show_start_ask_language() == 'f' and show_principles() == "encrypting":
        return screen_constants.FRENCH_ENCRYPTED_TEXT
    elif show_start_ask_language() == 'f' and show_principles() == "decrypting":
        return screen_constants.FRENCH_DECRYPTED_TEXT
    return 0


def show_language_settings():
    """
    shows the settings dialogue
    :return: None
    """
    language=input(screen_constants.LANGUAGE_SETTINGS)
    return language


def show_help_principles(english):
    """
    shows the help dialogue
    :return: None
    """
    if show_start_ask_language() == 'e':
        print(screen_constants.ENGLISH_HELP_PRINCIPLES)
    else:
        print(screen_constants.FRENCH_HELP_PRINCIPLES)


def show_quit_message(english):
    """
    shows the quit message
    :return: None
    """
    if show_start_ask_language() == 'e':
        print(screen_constants.ENGLISH_QUIT_MESSAGE)
    else:
        print(screen_constants.FRENCH_QUIT_MESSAGE)
