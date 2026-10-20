from first_call_claude import extract_text


def test_extract_text_skips_non_text_blocks():
    data = {
        "content": [
            {"type": "thinking", "thinking": "Let me think about this..."},
            {"type": "text", "text": "Hello!"},
        ]
    }

    result = extract_text(data)

    assert result == "Hello!"


def test_extract_text_joins_multiple_text_blocks():
    data = {
        "content": [
            {"type": "text", "text": "Hello, "},
            {"type": "text", "text": "world!"},
        ]
    }

    assert extract_text(data) == "Hello, world!"


def test_extract_text_empty_content():
    data = {"content": []}

    assert extract_text(data) == ""


def test_extract_text_missing_content():
    data = {}

    assert extract_text(data) == ""