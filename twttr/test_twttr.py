from twttr.twttr import shorten

def test_shorten():
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('Python') == 'Pythn'
    assert shorten('123!@#') == '123!@#'
    assert shorten('') == ''