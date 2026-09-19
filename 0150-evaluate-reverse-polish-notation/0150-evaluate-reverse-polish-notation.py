class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack: list[int] = []

        for i in range(0, len(tokens)):
            if tokens[i] == '+' or tokens[i] == '-' or tokens[i] == '*' or tokens[i] == '/':
                op1: int = stack.pop()
                op2: int = stack.pop()
                calc: int = 0

                if tokens[i] == '+':
                    calc = op1 + op2
                elif tokens[i] == '*':
                    calc = op1 * op2
                elif tokens[i] == '-':
                    calc = op2 - op1
                elif tokens[i] == '/':
                    calc = int(op2 / op1)

                stack.append(calc)
            else:
                stack.append(int(tokens[i]))

        return stack.pop()  
        