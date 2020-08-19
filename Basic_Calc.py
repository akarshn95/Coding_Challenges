def calculate(self, s):
        # we evaluate the preOp when the next Op is reached, so this is the dummy to operate last operand
        s += '+0'
        stack, preOp, num = [], '+', 0
        
        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char in ('+','-','*','/'):
                if preOp=='+': 
                    stack.append(num)
                elif preOp=='-':
                    stack.append(-num)
                elif preOp=='*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                preOp = char
                # since the number is operated upon, reset num
                num = 0
                
                
        return sum(stack)
