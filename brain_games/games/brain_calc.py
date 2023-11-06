#!/usr/bin/env python3


from random import choice
from brain_games.scripts.common_func import welcome_user, random


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
    user_name = welcome_user()
    print('What is the result of the expression?')
    right_answer_count = 0
    operations = ('*', '+', '-')

    while right_answer_count < 3:

        num1 = random()
        num2 = random()
        oper = choice(operations)
        res = result(oper, num1, num2)  # result of expression
        print(f'Question: {num1} {oper} {num2}')
        user_answer = input('Your answer: ')
        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f'{user_answer} is wrong answer.\n'
                  f'Correct answer was {res}\n'
                  f'Let\'s try again, {user_name}!')
            break

        if user_answer == res:
            print('Correct!')
            right_answer_count += 1
        else:
            print(f'{user_answer} is wrong answer.\n'
                  f'Correct answer was {res}\n'
                  f'Let\'s try again, {user_name}!')
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
