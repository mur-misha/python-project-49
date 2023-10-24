#!/usr/bin/env python3

from random import choice
from brain_games.common_func import welcome_user, random_num


def main():
    game()

def result(oper, a, b) -> int:
    if oper == '+':
        return int(a + b)
    elif oper == '-':
        return int(a - b)
    elif oper == '*':
        return int(a * b)


def game():

    operations = ('*', '+', '-')
    user_name = welcome_user()
    print('What is the result of the expression?')
    right_answer_count = 0

    while right_answer_count < 3:

        a = random_num()
        b = random_num()
        oper = choice(operations)
        print(f'Question: {a} {oper} {b}')
        user_answer = int(input())

        if user_answer == result(oper, a, b):
            print(f'Your answer: {user_answer}\nCorrect!')
            right_answer_count += 1
        else:
            print(f'Your answer: {user_answer}')
            print(f"'{user_answer}' is wrong answer. Correct answer was {result(oper, a, b)}\nLet's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
