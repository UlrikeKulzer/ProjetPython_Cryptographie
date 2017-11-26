import main_module
import text_module
import screen_module
import screen_constants


def test_format_and_normalise():
    text = "àâ test1t!? æ test2test,. ç test3test;+ èéêë test4test-% îï t5t$& ô test6test\"/ ùûü t7t{} ÿ t8t[] œ t9t= "
    print("***DEBUG***\nstart test from 'main_module' the functions 'format' and 'normalise'.\nTest text: ", text)
    print(main_module.format_text(text))


def test_caesar_encryption():
    key = 4
    text = "Hello world"
    print("***DEBUG***\nstart test from 'text_module' caesar encryption.\nTest key: ", key, ", test text:", text)
    print("***DEBUG*** result: ", text_module.encrypt_caesar(text, key))


test_caesar_encryption()