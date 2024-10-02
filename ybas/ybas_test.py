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


def test_labels():
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


def test_label_found_before_declaration():
    input_text = [
        '   TRAP on_error',
        '   PRINT "HELLO, WORLD!"',
        '   END',
        'on_error:',
        '   PRINT "ERROR!"',
    ]
    expected_output = [
        '10 TRAP 40',
        '20 PRINT "HELLO, WORLD!"',
        '30 END',
        '40 PRINT "ERROR!"'
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
