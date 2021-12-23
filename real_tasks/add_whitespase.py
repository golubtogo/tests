
def add_whitespase(s):
    return s + " "


def test_add_whitespase():
    s = ""
    s = add_whitespase(s)
    assert s == " "


test_add_whitespase()
