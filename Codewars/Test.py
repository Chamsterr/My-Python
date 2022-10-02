from ast import While
from collections import deque


def calc(expression):
    stack_o = []
    operations_codes = [40, 41, 42, 43, 45, 47]
    result_str = ''

    operations_priority = {
        "(": 1,
        ")": 1,
        "+": 2,
        "-" : 2,
        "*": 3,
        "/": 3
    }

    part_of_expression = [x for x in expression]
    while ' ' in part_of_expression: part_of_expression.remove(' ')

    for x in range(len(part_of_expression) - 1):
        if (part_of_expression[x] == '-' and part_of_expression[x+1] == '-'):
            part_of_expression[x] = '+'
            part_of_expression.pop(x+1)

    # if ord(x) in [40, 41, 42, 43, 45, 47]:
    for x in part_of_expression:
        if ord(x) not in [40, 41, 42, 43, 45, 47]: 
            result_str += x
        if ord(x) == 40:
            stack_o.append(x)
        if ord(x) in [42, 43, 45, 47]:

            if (len(stack_o) == 0 or ord(stack_o[-1]) == 40):
                stack_o.append(x)
                
            else:
                while len(stack_o) > 0 and operations_priority[x] <= operations_priority[stack_o[-1]]:
                    result_str += stack_o.pop()
                stack_o.append(x)
        if ord(x) == 41:
            while ord(stack_o[-1]) != 40:
                result_str += stack_o.pop()
            stack_o.pop()
    
    for x in range(len(stack_o)):
        result_str += stack_o.pop()

    deque = [x for x in result_str]
    
    while len(deque) > 1:
        a = int(deque.pop(0))
        b = int(deque.pop(0))
        operation = deque.pop(0)
        match operation:
             case "+":
                deque.insert(0, a + b)
             case "-":
                deque.insert(0, a - b)
             case "/":
                deque.insert(0, a / b)
             case "*":
                deque.insert(0, a * b)
    return deque[0]
print(calc('(2 + 5) * 2'))