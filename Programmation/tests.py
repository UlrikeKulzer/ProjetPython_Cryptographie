import main_module


def test_format_and_normalise():
    print("***DEBUG*** program is started")
    text = "àâ test1t!? æ test2test,. ç test3test;+ èéêë test4test-% îï t5t$& ô test6test\"/ ùûü t7t{} ÿ t8t[] œ t9t= "
    print("***DEBUG*** test text: ", text)
    print(main_module.format_text(text))
