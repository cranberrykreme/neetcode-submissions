class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def can_translate_to_digit(val) -> bool:
            try:
                int(val)
                return True
            except Exception:
                return False
        for token in tokens:
            if(can_translate_to_digit(token)):
                stack.append(int(token))
            else:
                item_one = stack.pop()
                item_two = stack.pop()
                match token:
                    case '+': 
                        stack.append(item_one + item_two)
                    case '-':
                        stack.append(item_two - item_one)
                    case '*':
                        stack.append(item_one * item_two)
                    case '/':
                        stack.append(int(item_two / item_one))
        return stack[0]
                    
