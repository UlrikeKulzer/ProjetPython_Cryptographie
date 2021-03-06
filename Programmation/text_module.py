"""
This module contains all functions with which the user's text can be treated.
"""


# ********************************* begin CAESAR ********************************* #
# *** ENCRYPTION *** #
def encrypt_caesar(text, key):
    """
    encrypts and returns the given text by using the principle of Caesar
    :param text: user's text (string)
    :param key: user's key (number)
    :return: text: encrypted text
    """
    encrypted_text = ''
    for i in text:
        # if by adding the key to the number of the letter,we go beyond the numbers between A and Z
        # we must go back to the beginning of the alphabet by using  - 26
        i = chr((ord(i) + key))
        if ord(i) > 90:
            i = chr(ord(i) - 26)
        encrypted_text += i
    return encrypted_text


# *** DECRYPTION *** #
def decrypt_caesar(text, key):
    """
    decrypts and returns the given text by using the principle of Caesar
    :param text: user's text (string)
    :param key: user's key (number)
    :return: text: decrypted text
    """
    decrypted_text = ''
    for i in text:
        # if by removing the key to the number of the letter, we go beyond the numbers between A and Z
        # we must go back to the beginning of the alphabet by using + 26
        i = chr((ord(i) - key))
        if ord(i) < 65:
            i = chr(ord(i) + 26)
        decrypted_text += i
    return decrypted_text


# ********************************** end CAESAR ********************************* #


# ********************************** begin VIGENERE ********************************* #
# *** HELP FUNCTIONS *** #
def create_vigenere_table():
    """
    creates a table 26x26 with the alphabet that recreates the Vigenere table
    :return: the table
    """
    alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    table = []
    for k in range(len(alphabet)):  # fill table
        # alphabet is shifted -1 in each row and column
        table += [alphabet[k:] + alphabet[:k]]
    return table


def create_table_text_key(text, key):
    """
    creates a table with the user's text in the first line and the repeated key in the second
    :param text: string
    :param key: string
    :return: table
    """
    key = key.upper()
    repeated_key = ""
    # we repeat the key until its length is bigger than the length of the text
    while len(repeated_key) < len(text):
        repeated_key += key
    list_key = []
    # in a table of two lines, we add in the first line the text and in the second line
    # the repeated key (same length as the text)
    for i in range(len(text)):
        list_temp = [text[i], repeated_key[i]]
        list_key.append(list_temp)
    return list_key


# *** ENCRYPTION *** #
def encrypt_vigenere(text, key):
    """
    encrypts and returns the given text by using the principle of Vigenere
    :param text: user's text (string)
    :param key: user's key (string)
    :return: text: encrypted text
    """
    table_of_vigenere = create_vigenere_table()
    repeated_key_table = create_table_text_key(text, key)
    encrypted_text = ""
    alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    for i in range(len(text)):
        # column corresponding to the letter of the text
        text_letter = repeated_key_table[i][0]
        # line corresponding to the letter of the key
        key_letter = repeated_key_table[i][1]
        encrypted_text += table_of_vigenere[alphabet.index(text_letter)][alphabet.index(key_letter)]
    return encrypted_text


# *** DECRYPTION *** #
def decrypt_vigenere(text, key):
    """
    decrypts and returns the given text by using the principle of Vigenere
    :param text: user's text (string)
    :param key: user's key (string)
    :return: text: decrypted text
    """
    vigenere_table = create_vigenere_table()
    repeated_key_table = create_table_text_key(text, key)
    decrypted_text = ""
    alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    for i in range(len(text)):
        # column corresponding to the letter of the text
        letter_text = repeated_key_table[i][0]
        # lign corresponding to the letter of the key
        letter_key = repeated_key_table[i][1]
        list_temp = vigenere_table[alphabet.index(letter_key)]
        decrypted_text += alphabet[list_temp.index(letter_text)]
    return decrypted_text


# ********************************* end VIGENERE ********************************* #


# ********************************* begin ENIGMA ********************************* #
# *** HELP FUNCTIONS *** #
# * Help functions * #
def create_initial_list():
    """
    creates a list filled with the alphabet (capital letters)
    :return: list
    """
    initial_list = [chr(x) for x in range(65, 91)]  # fill list thanks to Ascii code
    return initial_list


def search_index(initial_list, letter):
    """
    searches the index of a given letter in the given list
    :param initial_list: list for searching
    :param letter: index of this letter is wanted
    :return: index of the letter
    """
    i = 0
    # index initialized with 999 because
    # if something goes wrong in the loop the program stops after the execution of this function
    index = 999

    while i < len(initial_list):
        if initial_list[i] == letter:
            # if the given letter is found in the list, set the index to the actual position
            index = i
        i += 1
    else:
        # check if the index is out of range
        if (index < 0) or (index > len(initial_list)):
            index %= len(initial_list)
        # check if something went wrong before
        if index > len(initial_list):
            return "This should never happen"
        else:
            return index


def plugboard(letter):
    """
    represents the plugboard, i. e. checks if a given letter is plugged to another.
    If yes returns this letter, if no returns the given letter.
    :param letter: the given letter (char)
    :return: letter: either the plugged or the given letter (char)
    """
    # In this case the plugboard's setting is the one of the 31th of a month,
    # for more information see 'https://en.wikipedia.org/wiki/Enigma_rotor_details'
    # the plug combination is:
    # A-H, B-L, C-X, D-I, E-R, F-K, G-U, N-P, O-Q, T-Y
    # (J, M, S, V, W and Z not plugged)
    if letter in "JMSVWZ":
        return letter
    elif letter in "A":
        return "H"
    elif letter in "B":
        return "L"
    elif letter in "C":
        return "X"
    elif letter in "D":
        return "I"
    elif letter in "E":
        return "R"
    elif letter in "F":
        return "K"
    elif letter in "G":
        return "U"
    elif letter in "N":
        return "P"
    elif letter in "O":
        return "Q"
    elif letter in "T":
        return "Y"
    elif letter in "H":
        return "A"
    elif letter in "L":
        return "B"
    elif letter in "X":
        return "C"
    elif letter in "I":
        return "D"
    elif letter in "R":
        return "E"
    elif letter in "K":
        return "F"
    elif letter in "U":
        return "G"
    elif letter in "P":
        return "N"
    elif letter in "Q":
        return "O"
    elif letter in "Y":
        return "T"
    else:
        return "This should never happen"


def permutation_reflector(letter):
    """
    represents the reflector, i. e. returns the corresponding letter of the given letter
    :param letter: char
    :return: letter: char
    """
    # In this case the reflector's setting is the one of roller 'A',
    # for more information see 'https://en.wikipedia.org/wiki/Enigma_rotor_details'
    # the permutation is the following:
    # A-E, B-J, C-M, D-Z, F-L, G-Y, H-X, I-V, K-W, N-R, O-Q, P-U, S-T (and in the other direction)
    if letter in "A":
        return "E"
    elif letter in "B":
        return "J"
    elif letter in "C":
        return "M"
    elif letter in "D":
        return "Z"
    elif letter in "E":
        return "A"
    elif letter in "F":
        return "L"
    elif letter in "G":
        return "Y"
    elif letter in "H":
        return "X"
    elif letter in "I":
        return "V"
    elif letter in "J":
        return "B"
    elif letter in "K":
        return "W"
    elif letter in "L":
        return "F"
    elif letter in "M":
        return "C"
    elif letter in "N":
        return "R"
    elif letter in "O":
        return "Q"
    elif letter in "P":
        return "U"
    elif letter in "Q":
        return "O"
    elif letter in "R":
        return "N"
    elif letter in "S":
        return "T"
    elif letter in "T":
        return "S"
    elif letter in "U":
        return "P"
    elif letter in "V":
        return "I"
    elif letter in "W":
        return "K"
    elif letter in "X":
        return "H"
    elif letter in "Y":
        return "G"
    elif letter in "Z":
        return "D"
    else:
        return "This should never happen"


# * functions representing the rotors * #
def shift_first_rotor(return_path, index, offset):
    """
    represents the letter shift of the first rotor and returns the corresponding letter
    :param offset: int: represents the physical rotation of the rotor
    :param return_path: boolean: True if it's the return path (after the reflector) or False if it's the forward path
    :param index: the index of the actual letter
    :return letter: letter
    """
    # In this case the rotor's shift is the one of roller 'I',
    # for more information see 'https://en.wikipedia.org/wiki/Enigma_rotor_details'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotor1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    # shift_list calculates the shift of each letter between the alphabet and rotor1
    shift_list = [(ord(rotor1[i]) - ord(alphabet[i])) % len(alphabet) for i in range(len(alphabet))]
    letter = alphabet[index]
    if return_path is False:
        # assigns a new letter given the shift and the offset
        letter = alphabet[(index + shift_list[(index + offset) % len(alphabet)]) % len(alphabet)]
        if letter.isalpha():
            return letter
        else:
            print("This should never happen")
            return -1
    elif return_path:
        # sweeps the alphabet and tests for each letter
        for x in range(len(alphabet)):
            if letter == alphabet[(x + shift_list[(x + offset) % len(alphabet)]) % len(alphabet)]:
                letter = alphabet[x]
                return letter
            else:
                pass
        else:
            "This should never happen"


def shift_second_rotor(return_path, index, offset):
    """
    represents the letter shift of the second rotor and returns the corresponding letter
    :param offset: int: represents the physical rotation of the rotor
    :param return_path: boolean: True if it's the return path (after the reflector) or False if it's the forward path
    :param index: the index of the actual letter
    :return letter: letter
    """
    # In this case the rotor's shift is the one of roller 'II',
    # for more information see 'https://de.wikipedia.org/wiki/Enigma_(Maschine)'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    # shift_list calculates the shift of each letter between the alphabet and rotor2
    shift_list = [(ord(rotor2[i]) - ord(alphabet[i])) % len(alphabet) for i in range(len(alphabet))]
    letter = alphabet[index]
    if return_path is False:
        # assigns a new letter given the shift and the offset
        letter = alphabet[(index + shift_list[(index + offset) % len(alphabet)]) % len(alphabet)]
        if letter.isalpha():
            return letter
        else:
            print("This should never happen")
            return -1
    elif return_path:
        # sweeps the alphabet and tests for each letter
        for x in range(len(alphabet)):
            if letter == alphabet[(x + shift_list[(x + offset) % len(alphabet)]) % len(alphabet)]:
                letter = alphabet[x]
                return letter
            else:
                pass
        else:
            "This should never happen"


def shift_third_rotor(return_path, index, offset):
    """
    represents the letter shift of the third rotor and returns the corresponding letter
    :param offset: int: represents the physical rotation of the rotor
    :param return_path: boolean: True if it's the return path (after the reflector) or False if it's the forward path
    :param index: the index of the actual letter
    :return letter: letter
    """
    # In this case the rotor's shift is the one of roller 'III',
    # for more information see 'https://en.wikipedia.org/wiki/Enigma_rotor_details'
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotor3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    # shift_list calculates the shift of each letter between the alphabet and rotor3
    shift_list = [(ord(rotor3[i]) - ord(alphabet[i])) % len(alphabet) for i in range(len(alphabet))]
    letter = alphabet[index]
    if return_path is False:
        # assigns a new letter given the shift and the offset
        letter = alphabet[(index + shift_list[(index + offset) % len(alphabet)]) % len(alphabet)]
        if letter.isalpha():
            return letter
        else:
            print("This should never happen")
            return -1
    elif return_path:
        # sweeps the alphabet and tests for each letter
        for x in range(len(alphabet)):
            if letter == alphabet[(x + shift_list[(x + offset) % len(alphabet)]) % len(alphabet)]:
                letter = alphabet[x]
                return letter
            else:
                pass
    else:
        "This should never happen"


# *** EN/DECRYPTION *** #
def enigma(text, key):
    """
    encrypts or decrypts and returns the given text by using the principle of the Enigma machine
    :param text: user's text (string)
    :param key: user's key (string composed of three letter)
    :return text: encrypted text
    """
    initial_list = create_initial_list()

    # set the rotors according to the key
    offset_first_rotor = search_index(initial_list, key[0])
    offset_second_rotor = search_index(initial_list, key[1])
    offset_third_rotor = search_index(initial_list, key[2])

    encrypted_text = ""
    index_of_letter = 0
    return_path = False

    for letter in text:
        # ** forward path **
        return_path = False
        # plugboard
        letter = plugboard(letter)

        # determine index
        index_of_letter = search_index(initial_list, letter)
        # first rotor
        letter = shift_first_rotor(return_path, index_of_letter, offset_first_rotor)

        # determine index
        index_of_letter = search_index(initial_list, letter)
        # second rotor
        letter = shift_second_rotor(return_path, index_of_letter, offset_second_rotor)

        # determine index
        index_of_letter = search_index(initial_list, letter)
        # third rotor
        letter = shift_third_rotor(return_path, index_of_letter, offset_third_rotor)

        # permutation reflector
        letter = permutation_reflector(letter)

        # ** return path **
        return_path = True
        # determine index
        index_of_letter = search_index(initial_list, letter)
        # third rotor
        letter = shift_third_rotor(return_path, index_of_letter, offset_third_rotor)

        # determine index
        index_of_letter = search_index(initial_list, letter)
        # second rotor
        letter = shift_second_rotor(return_path, index_of_letter, offset_second_rotor)

        # determine index
        index_of_letter = search_index(initial_list, letter)
        # first rotor
        letter = shift_first_rotor(return_path, index_of_letter, offset_first_rotor)

        # plugboard
        letter = plugboard(letter)

        # add encrypted letter to the encrypted text
        encrypted_text = encrypted_text + letter

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

    return encrypted_text  # ********************************* end ENIGMA ********************************* #

