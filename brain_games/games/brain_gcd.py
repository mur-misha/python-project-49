#!/usr/bin/env python3

from brain_games.scripts.common_func import welcome_user, random


def main():
    brain_gcd()


def common_divisor(a, b):
    div1 = []
    div2 = []
    for i in range(1, a + 1):
        div1.append(a / i)
    for i in range(1, b + 1):
        div2.append(b / i)
    divisor = int(max(list(set(div1).intersection(set(div2)))))
    return divisor


def brain_gcd():
    user_name = welcome_user()
    right_answer_count = 0
    print('Find the greatest common divisor of given numbers.')

    while right_answer_count < 3:
        num1 = random()
        num2 = random()
        print(f'Question: {num1} {num2}')
        user_answer = input('Your answer: ')

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f'{user_answer} is wrong answer.\n'
                  f'Correct answer was {common_divisor(num1, num2)}\n'
                  f'Let\'s try again, {user_name}!')
            break

        if user_answer == common_divisor(num1, num2):
            print('Correct!')
            right_answer_count += 1
        else:
            print(f"'{user_answer}' is wrong answer;(.\n"
                  f"Correct answer was '{common_divisor(num1, num2)}'.\n"
                  f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
