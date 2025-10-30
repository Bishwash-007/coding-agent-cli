class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _apply_operator(self, operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        values.append(self.operators[operator](left, right))

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token.isdigit() or (token[0] == '-' and len(token) > 1 and token[1:].isdigit()):
                values.append(int(token))
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    self._apply_operator(operators, values)
                operators.pop()  # Pop the "("
            elif token in self.operators:
                while (operators and operators[-1] != "(" and
                       self.precedence.get(operators[-1], 0) >= self.precedence.get(token, 0)):
                    self._apply_operator(operators, values)
                operators.append(token)
            i += 1

        while operators:
            self._apply_operator(operators, values)

        return values[0] if values else 0