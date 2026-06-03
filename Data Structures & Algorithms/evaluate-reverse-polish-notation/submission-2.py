class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {'+','-','*','/'}:
                item_one = stack.pop()
                item_two = stack.pop()
                if token == '+': 
                    stack.append(item_two + item_one)
                elif token == '-':
                    stack.append(item_two - item_one)
                elif token ==  '*':
                    stack.append(item_two * item_one)
                else:
                    stack.append(int(item_two / item_one))
            else:
                stack.append(int(token))
        return stack[0]
                    
