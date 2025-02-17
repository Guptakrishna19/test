from index import add_numbers, concat_strings

def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_concat_strings():
    assert concat_strings('foo', 'bar') == 'foobar'
    assert concat_strings('hello', ' world') == 'hello world'
    assert concat_strings('', '') == ''

if __name__ == "__main__":
    test_add_numbers()
    test_concat_strings()
    print("All tests passed.")
#testing pull request...

# testing................
=======
# ;;;;;;;;;;;;;;;;;;

