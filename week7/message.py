
class InvalidMessageError(ValueError):
    """Raised when a Message has invalid data."""


class Message:
    ROLES = ("user", "assistant")

    def __init__(self, role, content):
        self.role = role
        self.content = content

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        if value not in Message.ROLES:
            raise InvalidMessageError(
                "Role must be 'user' or 'assistant'"
            )
        self._role = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if not isinstance(value, str) or not value.strip():
            raise InvalidMessageError(
                "Content must be a non-empty string"
            )
        self._content = value

    def __str__(self):
        return f"{self.role}: {self.content}"

    def to_dict(self):
        return {
            "role": self.role,
            "content": self.content,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            role=data.get("role"),
            content=data.get("content"),
        )
