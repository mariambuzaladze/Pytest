from paint import calculate

def test_calculate():
    assert calculate(70, 350) == 70
    assert calculate(350, 175) == 175
    assert calculate(100, 50) == 15
    assert calculate(10, 10) == 1
    assert calculate(0, 0) == 0
