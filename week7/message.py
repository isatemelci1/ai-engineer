from typing import TypedDict
from typing import Any

class MessageDict(TypedDict):
    role: str
    content: str


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

    def to_dict(self) -> MessageDict:
        return {
            "role": self.role,
            "content": self.content,
        }


    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Message":
        if "role" not in data or "content" not in data:
            raise InvalidMessageError(
                "Message data must contain 'role' and 'content'"
            )

        return cls(
            role=data["role"],
            content=data["content"],
        )
