def is_paired(input_string):
    braces = 0
    brackets = 0
    parens = 0

    symbol_stack = []

    for c in input_string:
        if c in ['{', '}', '[', ']', '(', ')']:        
            if len(symbol_stack) == 0:
                symbol_stack.append(c)
            else:
                if c in ['{', '[', '(']:
                    symbol_stack.append(c)
                elif c == '}':
                    if symbol_stack[-1] == '{':
                        symbol_stack = symbol_stack[:-1]
                    else:
                        return False
                elif c == ']':
                    if symbol_stack[-1] == '[':
                        symbol_stack = symbol_stack[:-1]
                    else:
                        return False
                elif c == ')':
                    if symbol_stack[-1] == '(':
                        symbol_stack = symbol_stack[:-1]
                    else:
                        return False

    return len(symbol_stack) == 0