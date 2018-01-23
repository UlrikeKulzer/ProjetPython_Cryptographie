"""
This module is responsible for the program flow.
In addition it is in charge of the formatting of the user's text.
"""

import screen_constants
import screen_module
import text_module
import ast  # to convert str to int


def format_key(key):
    key_list = [x for x in key]
    i = 0
    while i < len(key_list):
        # check if character is a digit
        if not key_list[i].isdigit():
            # if character is not a digit it is replaced by ''
            key_list[i] = ''
        i += 1
    else:
        # join the characters to a str to transform it to an int
        key = ''.join(key_list)
        key = ast.literal_eval(key)  # key has to be transformed from str to int
        return key


def normalise_letter(x):
    """
    normalisation of the given letter x if it is a special character
    the cases of French special characters and German "Umlaute" are shown
    :param: x is the given letter
    :return: chr
    """
    # checks if given character is part of the alphabet
    # if yes returns the letter, if not normalise it
    if ('a' <= x <= 'z') or ('A' <= x <= 'Z'):
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
    # all characters of the given text are saved in a list
    text_list = [x for x in text]
    i = 0
    while i < len(text_list):
        # check if character is part of the alphabet
        if text_list[i].isalpha():
            # call normalise function to normalise special characters
            text_list[i] = normalise_letter(text_list[i])
        else:
            # if character is not in the alphabet (such as digits) it is replaced by ''
            text_list[i] = ''
        i += 1
    else:
        # join the characters to a text to return it
        text = ''.join(text_list)
        # capitalise text
        text = text.upper()
        return text


def run():
    """
    starts the program
    :return: None
    """
    # initialise variables with default values (language: English, chosen mode: encryption)
    english = True
    encryption = True

    # set language
    if screen_module.show_start_ask_language() == 'f':
        english = False
    while True:
        # show main menu and set encryption variable
        main_menu = screen_module.show_main_menu(english)
        if main_menu == 'd':  # decryption
            encryption = False
        elif main_menu == 's':  # settings
            language = screen_module.show_language_settings()
            if language == 'f':  # change language to French
                english = False
                continue  # restart with the main menu (now in French)
            elif language == 'e':  # change language to English
                english = True
                continue  # restart with the main menu (now in English)
            else:
                print(screen_constants.INPUT_NOT_VALID)
                continue
        elif main_menu == 'q':  # quit program
            screen_module.show_quit_message(english)
            break  # stop program
        elif main_menu == 'c':
            pass
        else:
            print(screen_constants.INPUT_NOT_VALID)
            continue

        # set principle for en-/decryption
        principle = screen_module.show_principles(english, encryption)
        if principle == 'm':  # main menu
            continue  # go back to main menu
        elif principle == 'h':  # show help
            if english:
                print(screen_constants.ENGLISH_HELP_PRINCIPLES)
            elif not english:
                print(screen_constants.FRENCH_HELP_PRINCIPLES)
            screen_module.show_continue(english)
            continue
        else:
            # set key for en-/decryption
            key = screen_module.show_ask_key(english, principle)
            if key == 'm':  # main menu
                continue  # go back to main menu

            # format key if user failed
            if principle == 'c':  # if chosen principle is Caesar
                key = format_key(key)  # key is transformed into int

            # check if key is valid
            if principle == 'c' and (key > 25 or key < 1):
                print(screen_constants.INPUT_NOT_VALID)
                continue
            elif principle == 'v' and not key.isalpha():
                print(screen_constants.INPUT_NOT_VALID)
                continue
            elif principle == 'e' and (not key.isalpha() or len(key) != 3):
                print(screen_constants.INPUT_NOT_VALID)
                continue

            # set text for en-/decryption
            text = screen_module.show_ask_text(english)
            if text == 'm':  # main menu
                continue  # go back to main menu
            else:
                # format text
                text = format_text(text)
                # call en-/decryption function
                if principle == 'c':
                    if encryption:
                        text = text_module.encrypt_caesar(text, key)
                    else:
                        text = text_module.decrypt_caesar(text, key)
                elif principle == 'v':
                    if encryption:
                        text = text_module.encrypt_vigenere(text, key)
                    else:
                        text = text_module.decrypt_vigenere(text, key)
                elif principle == 'e':
                    text = text_module.enigma(text, key)
                else:
                    return "This should never happen"

        # show en/decrypted text
        if english:  # language chosen is english
            if encryption:
                print(screen_constants.ENGLISH_ENCRYPTED_TEXT + "\n" + text)  # print encrypted text
            elif not encryption:
                print(screen_constants.ENGLISH_DECRYPTED_TEXT + "\n" + text)  # print decrypted text
            else:
                return "This should never happen"
        elif not english:  # language chosen is french
            if encryption:
                print(screen_constants.FRENCH_ENCRYPTED_TEXT + "\n" + text)  # print encrypted text
            elif encryption is False:
                print(screen_constants.FRENCH_DECRYPTED_TEXT + "\n" + text)  # print decrypted text
            else:
                return "This should never happen"

        # program waits for the user's input and goes back to the main menu
        if screen_module.show_continue(english):
            continue  # start program


run()
