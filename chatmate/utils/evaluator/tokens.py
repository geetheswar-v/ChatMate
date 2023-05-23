from enum import Enum


class Token:

    def __init__(self, token, value):
        self.type = token.value
        self.value = value


class TokenType(Enum):
    NUMBER = 0
    OPERATOR = 1
    FUNCTION = 2
    PARENTHESIS = 3
