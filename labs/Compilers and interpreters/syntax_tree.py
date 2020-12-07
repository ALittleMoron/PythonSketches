"""
Лабораторная работа №3: генератор синтаксического дерева арифметических
выражений, обеспечивающего:
  а) возможность считывания анализируемого выраженияиз файла или ввода 
с клавиатуры;
  б) формирования и вывода на экран постфиксной и префиксной форм 
арифметического выражения.
  в) формирования и вывода на экран синтаксического дерева
введенного арифметического выражения.
"""

import sys
from pythonds.basic.stack import Stack
from typing import NamedTuple


PrefixForm, PostfixForm = str, str


class Form:
    """ класс инфикс -> постфикс- или инфикс -> префиксной формы. """
    def __init__(self):
        self.prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}


    def infixToPostfix(self, infixexpr) -> PostfixForm:
        """ Метод перевода инфиксной формы выражения в постфиксную. """
        opStack = Stack()
        postfixList = []
        tokenList = infixexpr.split()

        for token in tokenList:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfixList.append(token)
            elif token == '(':
                opStack.push(token)
            elif token == ')':
                topToken = opStack.pop()
                while topToken != '(':
                    postfixList.append(topToken)
                    topToken = opStack.pop()
            else:
                while (not opStack.isEmpty()) and \
                   (self.prec[opStack.peek()] >= self.prec[token]):
                      postfixList.append(opStack.pop())
                opStack.push(token)

        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return " ".join(postfixList)


    def infixToPrefix(self, infixexpr) -> PrefixForm:
        """ Метод перевода инфиксной формы выражения в префиксную. """
        return self.infixToPostfix(infixexpr)[::-1]


    def postfixEval(self, postfixExpr) -> int:
        """ Метод вычисления постфиксного выражения. """
        operandStack = Stack()
        tokenList = postfixExpr.split()

        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = self.doMath(token,operand1,operand2)
                operandStack.push(result)
        return operandStack.pop()


    def doMath(self, op, op1, op2):
        """ Метод вычисления в зависимости от оператора. """
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2


class SyntaxTree:
    def __init__(self):
        form = Form()


    def analyzing(self):
        pass


def main() -> None:
    check = True
    print("\nЛексический анализатор")
    while(check):
        choice = int(input("\nМеню:\n1. Запустить анализатор с введенной строкой\n2. Выйти из программы\nВыбор [1/2]: "))
        if (choice == 1):
            string = input('\nВведите строку для проверки: ')
            tree = SyntaxTree()
        elif (choice == 2):
            sys.exit()
        else:
            check = False


if __name__ == "__main__":
    main()