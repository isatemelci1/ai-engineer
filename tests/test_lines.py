import pytest
from lines import is_code_line


def test_blank_line():
    assert is_code_line("\n") == False


def test_whitespace_line():
    assert is_code_line("    \t\n") == False


def test_comment():
    assert is_code_line("# comment\n") == False


def test_indented_comment():
    assert is_code_line("    # comment\n") == False


def test_code():
    assert is_code_line("print('hello')\n") == True


def test_indented_code():
    assert is_code_line("    print('hello')\n") == True


def test_docstring():
    assert is_code_line('"""A docstring"""\n') == True