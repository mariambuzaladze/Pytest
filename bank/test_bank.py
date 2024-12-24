from bank.bank import value

def test_value():
    assert value('HeLlo World')=="$0"
    assert value(' h') == "$20"
    assert value('Hi')=="$20"
    assert value('anything')=="$100"