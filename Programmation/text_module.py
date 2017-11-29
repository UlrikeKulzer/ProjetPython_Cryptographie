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
    table = []
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
    table = [(x, key) for x in text]
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
def search_index(letter, alphabeth):
    return 0


def plugboard(letter):
    return 0


def shift_first_rotor(letter):
    return 0


def shift_second_rotor(letter):
    return 0


def shift_third_rotor(letter):
    return 0


def permutation_reflector(letter):
    return 0


# *** ENCRYPTION *** #
def encrypt_enigma(text, key):
    return_path = False
    initial_list = []
    first_rotor = []
    second_rotor = []
    third_rotor = []
    return 0


# *** DECRYPTION *** #
def decrypt_enigma(text, key):
    return_path = False
    initial_list = []
    first_rotor = []
    second_rotor = []
    third_rotor = []
    return 0

# ********** end ENIGMA ********** #
