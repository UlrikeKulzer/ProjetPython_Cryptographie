"""
This module is in charge of the user interface, i.e. it shows the right text in the chosen language.
"""

import screen_constants


def show_start_ask_language():
    """

    :return:
    """
    langue_choisie=input(START_ASK_LANGUAGE)
    return langue_choisie

def show_main_menu():
    if showStartAskLanguage()=='e':
        main_menu=input(ENGLISH_MAIN_MENU)
    elif showStartAskLanguage()=='f':
        main_menu=input(FRENCH_MAIN_MENU)
    if main_menu == 'c':
        return main_menu
    elif main_menu == 'd':
        encryptation = False
    elif main_menu == 's':
        language = str(input(LANGUAGE_SETTINGS)
        if language == 'e':
            english = True
        else:
            english = False
    elif main_menu == 'q':
        stop
    return 0

def show_principles():
    return 0

def show_ask_key():
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
        main_menu
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
