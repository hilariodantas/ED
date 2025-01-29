class Token:
    UNKNOWN = 0
    INT = 4
    MINUS = 5
    PLUS = 6
    MUL = 7
    DIV = 8
    FIRST_OP = 5

    def __init__(self, value):
        if isinstance(value, int):
            self.type = Token.INT
        else:
            self.type = self.makeType(value)
        self.value = value

    def isOperator(self):
        return self.type >= Token.FIRST_OP

    def __str__(self):
        return str(self.value)

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def makeType(self, ch):
        if ch == '*': return Token.MUL
        elif ch == '/': return Token.DIV
        elif ch == '+': return Token.PLUS
        elif ch == '-': return Token.MINUS
        else: return Token.UNKNOWN


class Scanner:
    def __init__(self, sourceStr):
        self.tokens = sourceStr.split()
        self.index = 0

    def hasNext(self):
        return self.index < len(self.tokens)

    def next(self):
        if not self.hasNext():
            raise Exception("No more tokens")
        token = self.tokens[self.index]
        self.index += 1
        try:
            return Token(int(token))
        except ValueError:
            return Token(token)


class PFEvaluator:
    def __init__(self, scanner):
        self.expressionSoFar = ""
        self.operandStack = []
        self.scanner = scanner

    def evaluate(self):
        while self.scanner.hasNext():
            currentToken = self.scanner.next()
            self.expressionSoFar += str(currentToken) + " "
            if currentToken.getType() == Token.INT:
                self.operandStack.append(currentToken.getValue())
            elif currentToken.isOperator():
                if len(self.operandStack) < 2:
                    raise ValueError("Too few operands on the stack")
                t2 = self.operandStack.pop()
                t1 = self.operandStack.pop()
                result = self.computeValue(currentToken, t1, t2)
                self.operandStack.append(result)
            else:
                raise ValueError("Unknown token type")
        if len(self.operandStack) > 1:
            raise ValueError("Too many operands on the stack")
        return self.operandStack.pop()

    def computeValue(self, op, value1, value2):
        if op.getType() == Token.PLUS:
            return value1 + value2
        elif op.getType() == Token.MINUS:
            return value1 - value2
        elif op.getType() == Token.MUL:
            return value1 * value2
        elif op.getType() == Token.DIV:
            if value2 == 0:
                raise ValueError("divide by zero")
            return value1 // value2
        else:
            raise ValueError("Unknown operator")

    def __str__(self):
        result = "\n"
        if self.expressionSoFar == "":
            result += "Portion of expression processed: none\n"
        else:
            result += "Portion of expression processed: " + self.expressionSoFar + "\n"
        if not self.operandStack:
            result += "The stack is empty"
        else:
            result += "Operands on the stack: " + str(self.operandStack)
        return result


class PFEvaluatorModel:
    def evaluate(self, sourceStr):
        self.evaluator = PFEvaluator(Scanner(sourceStr))
        return self.evaluator.evaluate()

    def format(self, sourceStr):
        scanner = Scanner(sourceStr)
        normalizedStr = ""
        while scanner.hasNext():
            normalizedStr += str(scanner.next()) + " "
        return normalizedStr.strip()

    def evaluationStatus(self):
        return str(self.evaluator)


class PFView:
    def __init__(self):
        self.model = PFEvaluatorModel()

    def run(self):
        while True:
            expression = input("Enter a postfix expression: ").strip()
            if not expression:
                break
            try:
                formattedExpr = self.model.format(expression)
                print(formattedExpr)
                value = self.model.evaluate(expression)
                print(value)
            except Exception as e:
                print("Error:", e)
                print(self.model.evaluationStatus())


# Iniciar o programa
if __name__ == "__main__":
    view = PFView()
    view.run()