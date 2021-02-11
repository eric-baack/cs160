#!/usr/bin/env python3
"""Stack exercise"""

from pythonds3.basic import Stack

## CS 160.  E Baack, March 2019
## Initial implementation was easy.  Challenge in implementing try / except
## Test module tested multiple functions - including do_math


class StackError(Exception):
    """Stack errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TokenError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class BaseError(Exception):
    """Token errors"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def rev_string(my_str):
    """Reverse characters in a string using a stack"""
    char_stack = Stack()
    for char in my_str:
        char_stack.push(char)
    new_chars = []
    while char_stack.size() > 0:
        new_chars.append(char_stack.pop())
    new_str = "".join(str(char) for char in new_chars)
    return new_str


def par_checker(line):
    """Textbook implementation"""
    stack = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol == "(":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        i = i + 1
    return balanced and stack.is_empty()


def par_checker_ext(line):
    """Check if parentheses & brackets are balanced"""
    stack = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol in "( { [ <":
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                sym2 = (
                    symbol.replace(")", "(")
                    .replace("]", "[")
                    .replace("}", "{")
                    .replace(">", "<")
                )
                if sym2 == stack.peek():
                    stack.pop()
                else:
                    balanced = False
        i = i + 1
    return balanced and stack.is_empty()


def par_checker_file(filename):
    """Check expressions in the file"""
    rfile = open(filename, "r")
    for line in rfile:
        balanced = par_checker_ext(line.strip())
        if balanced:
            print(f"{line.strip()} is balanced")
        else:
            print(f"{line.strip()} is NOT balanced")
    return


def base_converter(dec_num, base):
    """Convert a decimal number to any base"""
    digits = "0123456789ABCDEF"
    remstack = Stack()
    try:
        if base in (2, 8, 16):
            while dec_num > 0:
                rem = dec_num % base
                remstack.push(rem)
                dec_num = dec_num // base
            new_string = ""
            ctr = remstack.size()
            while ctr > 0:
                new_string = new_string + digits[remstack.pop()]
                ctr -= 1
            return new_string
        else:
            raise BaseError
    except BaseError:
        print("Invalid base:  only 2, 8, or 16 may be used")


def rpn_calc(postfix_expr):
    """Evaluate a postfix expression"""

    operandStack = Stack()
    tokenList = postfix_expr.split()
    try:
        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            elif token in "+-*/":
                if operandStack.size() < 2:
                    raise StackError("Stack is empty")
                else:
                    operand2 = operandStack.pop()
                    operand1 = operandStack.pop()
                    result = doMath(token, operand1, operand2)
                    operandStack.push(result)
            else:
                raise TokenError(f"Unknown token: {token}")
        if operandStack.size() > 1:
            raise StackError("Stack is not empty")

    except TokenError as err:
        raise TokenError(f"{err}")
    except SyntaxError:
        raise SyntaxError("Invalid syntax")
    except StackError as err:
        raise StackError(f"{err}")
    else:
        return operandStack.pop()


def doMath(op, op1, op2):
    """ Implements math for RPN """
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op in "1234567890abcdef":
        raise SyntaxError(f"Invalid syntax")
    else:
        raise TokenError(f"Unknown token: {op}")


def main():
    """Main function"""

    par_checker_file("data/exercises/stacks/parentheses.txt")


if __name__ == "__main__":
    main()
