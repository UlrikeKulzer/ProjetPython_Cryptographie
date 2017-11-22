"""
This module is in charge of the user interface, i.e. it shows the right text in the chosen language.
"""

import screen_constants


def show_start_ask_language():
    """

    :return:
    """


def show_main_menu():


def show_principles():


def show_ask_key():


def show_ask_text():


def show_treated_text():


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
