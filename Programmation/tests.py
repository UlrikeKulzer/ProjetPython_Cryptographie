"""
This module contains all functions which are used to test the program code.
"""

# TODO: COMMENT CODE!!!


import main_module
import text_module
import screen_module
import screen_constants


# *** tests for the text_module ***
# * Caesar *
def test_caesar_encryption():
    """
    tests to see if encrypt_caesar(text, key) is working
    :return: encrypted text
    """
    key = 4
    text = "Hello world"
    text2 = main_module.format_text(text)
    print("***DEBUG***\nstart test from 'text_module' caesar encryption.\nTest key: ", key, ", test text:", text2)
    print("***DEBUG*** result: ", text_module.encrypt_caesar(text2, key))


# TODO test decryptage
def test_caesar_encryption():
    print("")


# * Vigenère *
def test_create_table_of_vigenere():
    """
    tests to see if create_table_of_vigenere is working
    :return: table of vigenere
    """
    print(text_module.create_vigenere_table())


def test_vigenere_encryptation():
    # TODO add description
    """

    :return:
    """
    key = "magique"
    text = "Hello world"
    text2 = main_module.format_text(text)
    print("***DEBUG***\nstart test from 'text_module' vigenere encryption.\nTest key: ", key, ", test text:", text2)
    print("***DEBUG*** result: ", text_module.encrypt_vigenere(text2, key))


# TODO test decryptage
def test_vigenere_decryptation():
    print("")


# * Enigma *
def test_enigma():
    # TODO add description
    """

    :return:
    """
    text_module.encrypt_enigma("A", "")


# *** tests for the main_module ***
def test_format_and_normalise():
    """
    tests to see if normalise_letter and format_text are working
    :return: formated text
    """
    text = "àâ test1t!? æ test2test,. ç test3test;+ èéêë test4test-% îï t5t$& ô test6test\"/ ùûü t7t{} ÿ t8t[] œ t9t= "
    print("***DEBUG***\nstart test from 'main_module' the functions 'format' and 'normalise'.\nTest text: ", text)
    print(main_module.format_text(text))
    print("test")


def test_run():
    print("")


# run all tests
def run_all_tests():
    # TODO add description
    """

    :return:
    """
    test_caesar_encryption()
    test_format_and_normalise()
    test_create_table_of_vigenere()
    print(text_module.create_initial_list())
    test_encrypt_enigma()
