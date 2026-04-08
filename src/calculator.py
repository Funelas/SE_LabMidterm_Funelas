OPERATORS = {"+", "-", "*", "/"}

class Calculator:
    def __init__(self):
        self._left = ""
        self._op = ""
        self._right = ""
        self._state = "left"  # "left" | "op" | "right" | "error"

    def _display(self) -> str:
        return self._left + self._op + self._right

    def is_error(self) -> bool:
        return self._state == "error"

    def _evaluate(self) -> str:
        try:
            result = eval(f"{self._left}{self._op}{self._right}")
            return str(int(result) if result == int(result) else result)
        except ZeroDivisionError:
            return "Error"

    def press_number(self, value: str) -> str:
        if self._state == "error":
            return "Error"
        if self._state == "left":
            self._left += value
        elif self._state == "op":
            self._state = "right"
            self._right = value
        else:
            self._right += value
        return self._display()

    def press_operator(self, op: str) -> str:
        if self._state == "error" or self._left == "":
            return self._display()
        if self._state == "right" and self._right != "":
            result = self._evaluate()
            if result == "Error":
                self._state = "error"
                return "Error"
            self._left = result
        self._op = op
        self._right = ""
        self._state = "op"
        return self._display()

    def evaluate(self) -> str:
        if self._state != "right" or self._right == "":
            return self._display()
        result = self._evaluate()
        if result == "Error":
            self._state = "error"
            return "Error"
        self._left = result
        self._op = self._right = ""
        self._state = "left"
        return self._display()

    def delete(self) -> str:
        if self._state == "error":
            return "Error"
        if self._state == "right":
            self._right = self._right[:-1]
            if self._right == "":
                self._state = "op"
        elif self._state == "op":
            self._op = ""
            self._state = "left"
        else:
            self._left = self._left[:-1]
        return self._display()

    def clear(self) -> str:
        self._left = self._op = self._right = ""
        self._state = "left"
        return self._display()
