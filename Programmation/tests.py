import main_module
import text_module

# import screen_module
# import screen_constants


def test_format_and_normalise():
    text = "àâ test1t!? æ test2test,. ç test3test;+ èéêë test4test-% îï t5t$& ô test6test\"/ ùûü t7t{} ÿ t8t[] œ t9t= "
    print("***DEBUG***\nstart test from 'main_module' the functions 'format' and 'normalise'.\nTest text: ", text)
    print(main_module.format_text(text))
    print("test")


def test_caesar_encryption():
    key = 4
    text = "Hello world"
    text2 = main_module.format_text(text)
    print("***DEBUG***\nstart test from 'text_module' caesar encryption.\nTest key: ", key, ", test text:", text2)
    print("***DEBUG*** result: ", text_module.encrypt_caesar(text2, key))


def test_create_table_of_vigenere():
    print(text_module.create_table_of_vigenere())

def test_vigenere_encryptation():


test_caesar_encryption()
# test_format_and_normalise()
# test_create_table_of_vigenere()
# print(text_module.create_initial_list())
