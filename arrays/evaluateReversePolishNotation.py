class Solution(object):
    def evalRPN(self, tokens):
        i = 0
        if len(tokens) == 1:
            return int(tokens[0])
        expressions = ['+', '-', '/', '*']
        processed_tokens = []
        for token in tokens:
            if token in expressions:
                previous_previous_ele = processed_tokens.pop()
                previous_ele = processed_tokens.pop()
                if i >= 2 and self.isInt(previous_ele) and self.isInt(previous_previous_ele):
                    result = self.processExpression(token, int(previous_ele), int(previous_previous_ele))
                    processed_tokens.append(str(result))
                else:
                    processed_tokens.append(token)
            else:
                processed_tokens.append(token)
            i += 1
        return self.evalRPN(processed_tokens)

    def isInt(self, s):
        try:
            return True
        except ValueError:
            return False

    def processExpression(self, expression, int1, int2):
        if expression == '+':
            return int1 + int2
        elif expression == '-':
            return int1 - int2
        elif expression == '*':
            return int1 * int2
        else:
            return int(int1 / int2)


tokens_list = [["2","1","+","3","*"],["4","13","5","/","+"],["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]

for tokens in tokens_list:
    print(Solution().evalRPN(tokens))
