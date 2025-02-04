# Cookie Jar


class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity
        self.num = 0

    def __str__(self):
        return "🍪" * self.num

    def deposit(self, n):
        if not isinstance(n, int) or n < 0 or self.num + n > self._capacity:
            raise ValueError("Cannot deposit more than capacity.")
        self.num += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0 or self.num - n < 0:
            raise ValueError("Cannot withdraw more than available.")
        self.num -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.num
