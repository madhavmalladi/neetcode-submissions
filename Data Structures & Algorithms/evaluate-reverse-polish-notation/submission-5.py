class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ["1", "2" ,"3", "+", "-"]
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token in operators:
                second_val = int(stack.pop())
                first_val = int(stack.pop())
                if (token == "+"):
                    stack.append(first_val + second_val)
                elif (token =="-"):
                    stack.append(first_val - second_val)
                elif (token == "*"):
                    stack.append(first_val * second_val)
                else:
                    stack.append(int(first_val / second_val))
            else:
                stack.append(token)

        return int(stack.pop())