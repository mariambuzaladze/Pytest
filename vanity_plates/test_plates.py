from plates import is_valid

def test_is_valid():
    assert is_valid('CS50')==True
    assert is_valid('4cd')==False
    assert is_valid('AA05')==False
    assert is_valid('MB444')==True
    assert is_valid('Abcd1234')==False