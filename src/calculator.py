class Calculator:
    def __init__(self):
        self._expression = ""

    def press(self, value: str) -> str:
        self._expression += value
        return self._expression

    def delete(self) -> str:
        self._expression = self._expression[:-1]
        return self._expression

    def clear(self) -> str:
        self._expression = ""
        return self._expression
