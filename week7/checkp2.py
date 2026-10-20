
from typing import Any


class InvalidMessageError(ValueError):
    """Raised when a Message has invalid data."""


class Message:
    ROLES = ("user", "assistant")

    def __init__(self, role: str, content: str) -> None:
        self.role = role
        self.content = content

    @property
    def role(self) -> str:
        return self._role

    @role.setter
    def role(self, value: str) -> None:
        if value not in Message.ROLES:
            raise InvalidMessageError(
                "Role must be 'user' or 'assistant'"
            )
        self._role = value

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise InvalidMessageError(
                "Content must be a non-empty string"
            )
        self._content = value

    def __str__(self) -> str:
        return f"{self.role}: {self.content}"

    def to_dict(self) -> dict[str, str]:
        return {
            "role": self.role,
            "content": self.content,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Message":
        return cls(**data)


# 1. Create a conversation
messages: list[Message] = [
    Message("user", "Hi!"),
    Message("assistant", "Hello! How can I help?"),
    Message("user", "Explain Python list comprehensions."),
    Message("assistant", "They provide a concise way to build lists."),
]

# 2. Convert all messages into dictionaries for the LLM API
payload = [m.to_dict() for m in messages]

print("Full API payload:")
print(payload)

# 3. Keep only user messages
user_messages = [
    m.to_dict()
    for m in messages
    if m.role == "user"
]

print("\nUser messages only:")
print(user_messages)
