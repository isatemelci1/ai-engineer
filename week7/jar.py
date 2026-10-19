
class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or isinstance(capacity, bool):
            raise ValueError("Capacity must be a non-negative integer")

        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if not isinstance(n, int) or isinstance(n, bool):
            raise ValueError("Number of cookies must be a non-negative integer")

        if n < 0:
            raise ValueError("Number of cookies must be a non-negative integer")

        if self.size + n > self.capacity:
            raise ValueError("Jar capacity exceeded")

        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or isinstance(n, bool):
            raise ValueError("Number of cookies must be a non-negative integer")

        if n < 0:
            raise ValueError("Number of cookies must be a non-negative integer")

        if n > self.size:
            raise ValueError("Not enough cookies in the jar")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
