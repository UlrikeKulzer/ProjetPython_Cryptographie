"""
This module is in charge of the user interface, i.e. it shows the right text in the chosen language.
"""

import screen_constants


def showStartAskLanguage():
    langue_choisie=input(screen_constants.START_ASK_LANGUAGE)
    return langue_choisie

def show_main_menu():
    if showStartAskLanguage() == 'e':
        main_menu = input(screen_constants.ENGLISH_MAIN_MENU)
    elif showStartAskLanguage() == 'f':
        main_menu = input(screen_constants.FRENCH_MAIN_MENU)
    return main_menu


def show_principles():
    if show_main_menu() == 'c':
        crypting = input(screen_constants.ENGLISH_PRINCIPLES_ENCRYPTING)
        return crypting
    elif show_main_menu() == 'd':
        decrypting = input(screen_constants.ENGLISH_PRINCIPLES_DECRYPTING)
        return decrypting
    elif show_main_menu() == 's':
        language = input(screen_constants.LANGUAGE_SETTINGS)
        return language


def show_ask_key():
    if show_principles() == 'c'
        key = input(screen_constants.ENGLISH_ASK_KEY_CAESAR)
        return key
    elif show_principles() == 'v'
        key = input(screen_constants.ENGLISH_ASK_KEY_VIGENERE)
        return key
    elif show_principles() == 'e'
        key = input(screen_constants.ENGLISH_ASK_KEY_ENIGMA)
        return key
    elif show_principles() == 'm'
        main_menu = input(screen_constants.ENGLISH_MAIN_MENU)
        return main_menu



def show_ask_key():
    if cesar = true and english = true:
        return screen_constants.ENGLISH_ASK_KEY_CAESAR


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
