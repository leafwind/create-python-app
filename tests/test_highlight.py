from app.highlight import highlight


def test_highlight():
    input_str = "test"
    expected = input_str
    actual = highlight(input_str, "pink")
    assert expected == actual

    input_str = "test"
    expected = "\x1b[31mtest\x1b[0m"
    actual = highlight(input_str, "red")
    print(actual)
    assert expected == actual
