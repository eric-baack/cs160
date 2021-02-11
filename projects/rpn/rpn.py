#!/usr/bin/env python3
"""
Reverse Polish Notation
"""

from pythonds3.basic import Stack


# Status Feb 26.  Mostly working.  Need to revisit try / except structure in postfix_eval
# Checksum addition is correct.
# Attempted to revise error trapping - not quite working.  When stack lacking operands
# should raise error - but it does not do so correctly.


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        """Initializer"""
        Exception.__init__(self, *args, **kwargs)


def postfix_eval(postfix_expr: str) -> int:
    """ evaluate postfix expressions in a string """
    operandStack = Stack()
    tokenList = postfix_expr.split()
    try:
        for token in tokenList:
            if token.isnumeric():
                operandStack.push(int(token))
            elif token in "* ** / // % + -":
                ## this if statement is not working - why not?
                if operandStack.size() < 2:
                    raise SyntaxError("invalid syntax")
                else:
                    operand2 = operandStack.pop()
                    operand1 = operandStack.pop()
                    result = do_math(token, operand1, operand2)
                    operandStack.push(result)
            elif token == "=":
                if operandStack.size() > 1:
                    raise StackError("Stack is not empty")
                elif operandStack.size() == 0:
                    raise StackError("Stack is empty")
                else:
                    return operandStack.pop()
            else:
                raise TokenError(f"Unknown token: {token}")
    except ZeroDivisionError as err:
        raise ZeroDivisionError(f"{err}")
    except SyntaxError:
        raise SyntaxError(f"Invalid syntax")
    except TokenError as err:
        raise TokenError(f"{err}")


def do_math(op: str, op1: int, op2: int) -> int:
    """ implement mathematical operations using operator and two operands"""
    if op == "**":
        return op1 ** op2
    elif op == "//":
        try:
            return op1 // op2
        except:
            raise ZeroDivisionError("integer division or modulo by zero")
    elif op == "*":
        return op1 * op2
    elif op == "/":
        try:
            return op1 / op2
        except:
            raise ZeroDivisionError("division by zero")
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "%":
        try:
            return op1 % op2
        except:
            raise ZeroDivisionError("integer division or modulo by zero")
    elif isinstance(op, int):
        raise SyntaxError(f"invalid syntax")
    elif isinstance(op, str):
        raise SyntaxError(f"invalid syntax")
    else:
        raise TokenError(f"Invalid token: {op}")


def rpn_calc(filename: str) -> int:
    """ rpn calculator:  evaluates post-fix expressions """
    file_read = open(filename, "r")
    checksum = 0
    for line in file_read:
        try:
            answer = postfix_eval(line)
            checksum = checksum + answer
            print(line.strip(), answer)
        except Exception as inst:
            print(line.strip(), inst)
    return checksum


def main():
    """Main function"""
    checksum = rpn_calc("data/projects/rpn/rpn_input_2.txt")
    print(f"Checksum is {checksum:.2f}")


if __name__ == "__main__":
    main()
