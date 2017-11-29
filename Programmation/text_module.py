"""
This module contains all functions with which the user's text can be treated.
"""


# ********** begin CAESAR ********** #
# *** ENCRYPTION *** #
def encrypt_caesar(text, key):
    """

    :param text:
    :param key:
    :return:
    """
    crypted_text = ''
    for i in text:
        if ord(i) + key > 90:
            i = chr(ord('A') - 1 + (key - (ord('Z') - ord(i))))
            crypted_text += i
        else:
            i = chr(ord(i) + key)
            crypted_text += i
    return crypted_text


# *** DECRYPTION *** #
def decrypt_caesar(text, key):
    decrypted_text = ''
    for i in text:
        if ord(i) - key < 65:
            i = chr(ord('Z') + 1 - (key - (ord(i) - ord('A'))))
            decrypted_text += i
        else:
            i = chr(ord(i) - key)
            decrypted_text += i
    return decrypted_text


# ****** end CAESAR ****** #


# ********** begin VIGENERE ********** #
# *** HELP FUNCTIONS *** #
def create_table_of_vigenere():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    table = []
    for k in range(25):
        table += [alphabet[k:] + alphabet[:k]]
    return table


def repeat_key(key):
    return


def create_table_text_key(text, key):
    """
    creates a table with the user's text in the first line and the repeated key in the second
    :param text: string
    :param key: string
    :return: table
    """
    table = [(x, key) for x in text]  # NOT FINISHED
    return table


# *** ENCRYPTION *** #
def encrypt_vigenere(text, key):
    table_of_vigenere = create_table_of_vigenere()
    repeated_key_table = create_table_text_key(text, key)

    return text


# *** DECRYPTION *** #
def decrypt_vigenere(text, key):
    return text


# ****** end VIGENERE ****** #


# ********** begin ENIGMA ********** #
# *** HELP FUNCTIONS *** #
def create_initial_list():
    """
    creates a list filled with the alphabet
    :return: list
    """
    # real list:
    # initial_list = [chr(x) for x in range(65, 91)]
    # for test purpose used letters are only "A - F"
    initial_list = [chr(x) for x in range(65, 71)]
    return initial_list


def search_index(initial_list, letter):
    return 0


def plugboard(letter):
    """
    represents the plugboard, i. e. checks if a given letter is plugged to another.
    If yes returns this letter, if no returns the given letter.
    :param letter: the given letter (char)
    :return: letter: either the plugged or the given letter (char)
    """
    # for test purpose the plug combination for A - F is:
    # A-C, B-F, C-A, D-, E-, F-B (D and E not plugged)
    if letter in "DE":
        return letter
    elif letter in "A":
        return "C"
    elif letter in "B":
        return "F"
    elif letter in "C":
        return "A"
    elif letter in "F":
        return "B"
    else:
        return "This should never happen"


def shift_first_rotor(initial_list, return_path, letter):
    """
    represents the letter shift of the first rotor and returns the corresponding letter
    :param initial_list: list on which the function operates to
    :param return_path: indicates if the letter already passed the reflector
    :param letter: the given letter (char)
    :return: letter
    """

    return 0


def shift_second_rotor(initial_list, return_path, letter):
    return 0


def shift_third_rotor(initial_list, return_path, letter):
    return 0


def permutation_reflector(letter):
    """
    represents the reflector, i. e. returns the corresponding letter of the given letter
    :param letter: char
    :return: letter: char
    """
    # for test purpose the reflector combination for A - F is:
    # A-D, B-E, C-F, D-A, E-B, F-C
    if letter in "A":
        return "D"
    elif letter in "B":
        return "E"
    elif letter in "C":
        return "F"
    elif letter in "D":
        return "A"
    elif letter in "E":
        return "B"
    elif letter in "F":
        return "C"
    else:
        return "This should never happen"


# *** ENCRYPTION *** #
def encrypt_enigma(text, key):
    """
    encrypts and returns the given text by using the principle of the Enigma machine
    :param text: user's text (string)
    :param key:
    :return: text
    """
    return_path = False
    initial_list = create_initial_list()
    offset_first_rotor = 0
    offset_second_rotor = 0
    offset_third_rotor = 0
    encrypted_text = ""

    for x in text:
        x = plugboard(x)
        x = shift_first_rotor(initial_list, return_path, x)

        # change offset variables
        offset_first_rotor += 1
        if offset_first_rotor == len(initial_list):
            offset_first_rotor = 0
            offset_second_rotor += 1
            if offset_second_rotor == len(initial_list):
                offset_second_rotor = 0
                offset_third_rotor += 1
                if offset_third_rotor == len(initial_list):
                    offset_third_rotor = 0
                else:
                    pass
            else:
                pass
        else:
            pass

        x = shift_second_rotor(initial_list, return_path, x)
        x = shift_third_rotor(initial_list, return_path, x)
        x = permutation_reflector(x)
        return_path = True
        x = shift_third_rotor(initial_list, return_path, x)
        x = shift_second_rotor(initial_list, return_path, x)
        x = shift_first_rotor(initial_list, return_path, x)
        x = plugboard(x)
        return_path = False
        encrypted_text = encrypted_text + x
    return encrypted_text


# *** DECRYPTION *** #
def decrypt_enigma(text, key):
    return_path = False
    initial_list = create_initial_list()
    first_rotor = []
    second_rotor = []
    third_rotor = []
    return 0

# ********** end ENIGMA ********** #
