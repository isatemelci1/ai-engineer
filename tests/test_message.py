import pytest
from message import Message


def test_invalid_role_after_creation():
    msg = Message("user", "Hello")

    with pytest.raises(ValueError):
        msg.role = "admin"


def test_invalid_content_after_creation():
    msg = Message("user", "Hello")

    with pytest.raises(ValueError):
        msg.content = ""


def test_none_content_at_creation():
    with pytest.raises(ValueError):
        Message("user", None)


def test_whitespace_content_after_creation():
    msg = Message("user", "Hello")

    with pytest.raises(ValueError):
        msg.content = "   "


def test_valid_role_update():
    msg = Message("user", "Hello")
    msg.role = "assistant"

    assert msg.role == "assistant"


def test_valid_content_update():
    msg = Message("user", "Hello")
    msg.content = "Updated"

    assert msg.content == "Updated"


def test_to_dict():
    msg = Message("user", "Hello")

    assert msg.to_dict() == {
        "role": "user",
        "content": "Hello",
    }


def test_from_dict():
    data = {"role": "assistant", "content": "Hi"}

    msg = Message.from_dict(data)

    assert msg.role == "assistant"
    assert msg.content == "Hi"



def test_round_trip():
    original = Message("user", "Hello")

    restored = Message.from_dict(original.to_dict())

    assert restored.role == original.role
    assert restored.content == original.content


def test_from_dict_missing_content():
    data = {"role": "user"}

    with pytest.raises(ValueError):
        Message.from_dict(data)



def test_from_dict_invalid_role():
    data = {"role": "admin", "content": "Hello"}

    with pytest.raises(ValueError):
        Message.from_dict(data)


def test_from_dict_invalid_content():
    data = {"role": "user", "content": None}

    with pytest.raises(ValueError):
        Message.from_dict(data)

def test_from_dict_missing_role():
    with pytest.raises(ValueError):
        Message.from_dict({"content": "Hello"})