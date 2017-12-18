"""
This module is in charge of the user interface, i.e. it shows the right text in the chosen language.
"""


import screen_constants


def show_start_ask_language():
    """
    asks the language the user wants to use at the beginning:french or english
    ' f ' for french
    ' e ' for english
    :return: char
    """
    return input(screen_constants.START_ASK_LANGUAGE)


def show_language_settings():
    """
    asks the language the user wants to use in the program : french or english
    ' f ' for french
    ' e ' for english
    :return: char
    """
    return input(screen_constants.LANGUAGE_SETTINGS)


def show_main_menu(english):
    """
    asks the user if he wants to use the fonction encryption or decryption of the program
    'c' for encryption
    'd' for decryption
    's' for going to language settings
    'q' to quit the program
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :return: char
    """
    #language chosen is english
    if english:
        return input(screen_constants.ENGLISH_MAIN_MENU)
    #language chosen is french
    elif english == False:
        return input(screen_constants.FRENCH_MAIN_MENU)
    else:
        return "this should never happen"


def show_principles(english, encrypting):
    """
    asks what type of method the user wants to use to encrypt or decrypt his text
    'c' for Caesar's cypher
    'v' for Vigenere's cypher
    'e' for the Enigma machine
    'm' to go back to the main menu
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :param encrypting: boolean
    True if the user wants to encrypt his text
    False if he wants to decrypt his text
    :return: char
    """
    # language chosen is english
    if english:
        if encrypting:
            return input(screen_constants.ENGLISH_PRINCIPLES_ENCRYPTING)
        if encrypting == false:
            return input(screen_constants.ENGLISH_PRINCIPLES_DECRYPTING)
    # language chosen is french
    elif english == False:
        if encrypting:
            return input(screen_constants.ENGLISH_PRINCIPLES_ENCRYPTING)
        if encrypting == false:
            return input(screen_constants.ENGLISH_PRINCIPLES_DECRYPTING)
    else:
        return "this should never happen"


def show_ask_key(english):
    """
    asks the key the user wants to use for the method his has chosen
    key = char
    ' m ' to go back to the main menu
    ' r ' to go back to the previous menu
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :return: char
    """
    # language chosen is english
    if english:
        if caesar:
            return input(screen_constants.ENGLISH_ASK_KEY_CAESAR)
        elif vigenere:
            return input(screen_constants.ENGLISH_ASK_KEY_VIGENERE)
        elif enigma:
            return input(screen_constants.ENGLISH_ASK_KEY_ENIGMA)
        else:
            return "this should never happen"
    # language chosen is french
    elif english == False:
        if caesar:
            return input(screen_constants.FRENCH_ASK_KEY_CAESAR)
        elif vigenere:
            return input(screen_constants.FRENCH_ASK_KEY_VIGENERE)
        elif enigma:
            return input(screen_constants.FRENCH_ASK_KEY_ENIGMA)
        else:
            return "this should never happen"


def show_ask_text(english):
    """
    asks the text that the user wants to decrypt/encrypt
    ' m ' to go back to the main menu
    ' r ' to go back to the previous menu
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :return: char
    """
    # language chosen is english
    if english:
        return input(screen_constants.ENGLISH_ASK_TEXT)
    # language chosen is french
    elif english == False:
        return input(screen_constants.FRENCH_ASK_TEXT)
    else:
        return "this should never happen"


def show_treated_text(english, encrypting):
    """
    shows the decrypt/encrypt text
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :param encrypting: boolean
    True if the user wants to encrypt his text
    False if he wants to decrypt his text
    :return: char
    """
    # language chosen is english
    if english:
        if encrypting:
            print(screen_constants.ENGLISH_ENCRYPTED_TEXT)
        elif encrypting == False:
            print(screen_constants.ENGLISH_DECRYPTED_TEXT)
    # language chosen is french
    if english == False:
        if encrypting:
            print(screen_constants.FRENCH_ENCRYPTED_TEXT)
        elif encrypting == False:
            print(screen_constants.FRENCH_DECRYPTED_TEXT)
    else:
        return "this should never happen"

def show_help_principles(english):
    """
    shows the help screen which give explanations on the different encryption methods
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :return: char
    """
    # language chosen is english
    if english:
        print(screen_constants.ENGLISH_HELP_PRINCIPLES)
    # language chosen is french
    elif english==False:
        print(screen_constants.FRENCH_HELP_PRINCIPLES)
    else:
        return "this should never happen"

def show_quit_message(english):
    """
    shows the exit message of the program
    :param english: boolean
     True if chosen language is english
     False if chosen language is french
    :return: char
    """
    # language chosen is english
    if english:
        print(screen_constants.ENGLISH_QUIT_MESSAGE)
    # language chosen is french
    elif english == False:
        print(screen_constants.FRENCH_QUIT_MESSAGE)
    else:
        return "this should never happen"
