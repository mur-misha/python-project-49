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

    user_name = welcome_user()
    print('What is the result of the expression?')
    right_answer_count = 0
    operations = ('*', '+', '-')

    while right_answer_count < 3:

        a = random_num()
        b = random_num()
        oper = choice(operations)
        res = result(oper, a, b)
        print(f'Question: {a} {oper} {b}')
        user_answer = input()
        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f'Your answer: {user_answer}\n'
                  f'{user_answer} is wrong answer. Correct answer was {res}\n'
                  f'Let\'s try again, {user_name}!')
            break

        if user_answer == res:
            print(f'Your answer: {user_answer}\nCorrect!')
            right_answer_count += 1
        else:
            print(f'Your answer: {user_answer}\n'
                  f'{user_answer} is wrong answer. Correct answer was {res}\n'
                  f'Let\'s try again, {user_name}!')
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
