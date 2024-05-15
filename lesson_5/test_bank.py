from bank import checkInput

def test_greeting_hello():
    assert checkInput("hello") == "$0"

def test_h_greeting():
    assert checkInput("hi there :)") == "$20"

def test_non_h_greeting():
    assert checkInput("What's going on? ") == "$100"