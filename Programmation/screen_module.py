"""
This module is in charge of the user interface, i.e. it shows the right text in the chosen language.
"""

import screen_constants


def show_start_ask_language():
    """

    :return:
    """


def show_main_menu():
    return 0

def show_principles():
    return 0

def show_ask_key():
    if cesar = true and english = true:
        return ENGLISH_ASK_KEY_CAESAR


    return 0

def show_ask_text():
    return 0

def show_treated_text():
    return 0

def show_language_settings():
    """
    prints the settings dialogue
    :return: None
    """
    print(screen_constants.language_settings)



def show_help_principles(english):
    """
    prints the help dialogue
    :return: None
    """
    if english:
        print(screen_constants.english_help_principles)
    else:
        print(screen_constants.french_help_principles)


def show_quit_message(english):
    """
    prints the quit message
    :return: None
    """
    if english:
        print(screen_constants.english_quit_message)
    else:
        print(screen_constants.french_quit_message)
