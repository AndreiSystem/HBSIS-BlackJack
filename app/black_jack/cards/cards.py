from abc import ABC

class Cards(ABC):
    def __init__(self, name: str, value: int):
        self._name = name
        self._value = value

    def get_value(self):
        return self._value

    def __str__(self):
        return self._name

class A(Cards):
    def __init__(self):
        super().__init__('A', 1)

class Q(Cards):
    def __init__(self):
        super().__init__('Q', 10)

class J(Cards):
    def __init__(self):
        super().__init__('J', 10)

class K(Cards):
    def __init__(self):
        super().__init__('K', 10)

class Um(Cards):
    def __init__(self):
        super().__init__('1', 1)

class Dois(Cards):
    def __init__(self):
        super().__init__('2', 2)

class Tres(Cards):
    def __init__(self):
        super().__init__('3', 3)

class Quatro(Cards):
    def __init__(self):
        super().__init__('4', 4)

class Cinco(Cards):
    def __init__(self):
        super().__init__('5', 5)


class Seis(Cards):
    def __init__(self):
        super().__init__('6', 6)


class Sete(Cards):
    def __init__(self):
        super().__init__('7', 7)


class Oito(Cards):
    def __init__(self):
        super().__init__('8', 8)

class Nove(Cards):
    def __init__(self):
        super().__init__('9', 9)


class Dez(Cards):
    def __init__(self):
        super().__init__('10', 10)




