
def test_concat_strings():
    assert concat_strings('foo', 'bar') == 'foobar'
    assert concat_strings('hello', ' world') == 'hello world'
    assert concat_strings('', '') == ''

if __name__ == "__main__":
    test_add_numbers()
    test_concat_strings()
    print("All tests passed.")

