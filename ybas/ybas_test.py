import pytest
from ybas import convert


def test_convert():
    ybas = [
        '    PRINT "HELLO, WORLD!"',
        '    PRINT "HELLO, AGAIN."',
    ]
    expected = [
        '10 PRINT "HELLO, WORLD!"',
        '20 PRINT "HELLO, AGAIN."',
    ]
    assert convert(ybas) == expected


def test_convert_with_labels():
    input_text = [
        'start:',
        '  PRINT "HELLO, WORLD!"',
        '  GOTO start'
    ]
    expected_output = [
        '10 PRINT "HELLO, WORLD!"',
        '20 GOTO 10'
    ]
    assert convert(input_text) == expected_output


def test_duplicate_label():
    input_text = [
        'start:',
        '  PRINT "HELLO, WORLD!"',
        'start:',
        '  GOTO start'
    ]
    with pytest.raises(ValueError, match='Duplicate label start found on line 3'):
        convert(input_text)
