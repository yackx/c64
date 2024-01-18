import io
import pytest
from y_acme_fmt import format


def test_label_col_1():
    input_data = io.StringIO("!addr {\n")
    expected_output = "!addr {\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_label_after_col_1():
    input_data = io.StringIO(" !addr {\n")
    expected_output = "            !addr {\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_code_col_13():
    input_data = io.StringIO("            lda #$0f\n")
    expected_output = "            lda #$0f\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_code_after_col_13():
    input_data = io.StringIO("                          lda #$0f\n")
    expected_output = "            lda #$0f\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_comment_alone_after_col_1():
    input_data = io.StringIO("; This is a test\n")
    expected_output = "; This is a test\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_comment_alone_col_13():
    input_data = io.StringIO("            ; Each entry is 3 bytes\n")
    expected_output = "            ; Each entry is 3 bytes\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_comment_alone_start_after_col_13():
    input_data = io.StringIO("                  ; Each entry is 3 bytes\n")
    expected_output = "                                            ; Each entry is 3 bytes\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_rstrip():
    input_data = io.StringIO(" !addr {   \n")
    expected_output = "            !addr {\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_label_col_1_comment_col_13():
    input_data = io.StringIO("main:       ; comment should not exist after label but ok\n")
    expected_output = "main:       ; comment should not exist after label but ok\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_label_col_1_comment_before_col_13():
    input_data = io.StringIO("main:  ; comment should not exist after label but ok\n")
    expected_output = "main:       ; comment should not exist after label but ok\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_label_col_1_comment_before_col_45():
    input_data = io.StringIO("main:                  ; comment should not exist after label but ok\n")
    expected_output = "main:                                       ; comment should not exist after label but ok\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_label_col_1_comment_col_45():
    input_data = io.StringIO("main:                                       ; comment should not exist after label but ok\n")
    expected_output = "main:                                       ; comment should not exist after label but ok\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_label_col_1_comment_after_col_45():
    input_data = io.StringIO("main:                      ; comment should not exist after label but ok\n")
    expected_output = "main:                                       ; comment should not exist after label but ok\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_label_col_1_code_before_col_13():
    input_data = io.StringIO("main: lda #$0f\n")
    expected_output = "main:       lda #$0f\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_label_plus_sign():
    input_data = io.StringIO("+           lda $01\n")
    expected_output = "+           lda $01\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_label_plus_plus_sign():
    input_data = io.StringIO("++          lda $01\n")
    expected_output = "++          lda $01\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_call_macro():
    input_data = io.StringIO("            +mem_init\n")
    expected_output = "            +mem_init\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_code_with_comment_before_col_45():
    input_data = io.StringIO("        ldy #0              ; memory page index\n")
    expected_output = "            ldy #0                          ; memory page index\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_code_before_col_13_with_comment_col_45():
    input_data = io.StringIO("    CINT = $ff81                            ; Clear screen\n")
    expected_output = "            CINT = $ff81                    ; Clear screen\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_dot_prefix_label_no_colon():
    input_data = io.StringIO(".mask   !byte 0\n")
    expected_output = ".mask       !byte 0\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_displaced_label():
    input_data = io.StringIO("            .target = * + 1\n")
    expected_output = "            .target = * + 1\n"
    output = format(input_data)
    assert output.getvalue() == expected_output


def test_displaced_label_with_comment():
    input_data = io.StringIO("            .src = *+2                      ; Self modifying\n")
    expected_output = "            .src = *+2                      ; Self modifying\n"
    output = format(input_data)
    assert output.getvalue() == expected_output

    

pytest.main()
