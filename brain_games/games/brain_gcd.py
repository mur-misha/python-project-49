#!/usr/bin/env python3

from brain_games.scripts.common_func import welcome_user, random


def main():
    brain_gcd()


def brain_gcd():
    user_name = welcome_user()
    right_answer_count = 0
    print('Find the greatest common divisor of given numbers.')

    while right_answer_count < 3:
        num1 = random()
        num2 = random()
        div1 = []
        div2 = []
        print(f'Question: {num1} {num2}')

        for i in range(1, num1 + 1):
            div1.append(num1 / i)
        for i in range(1, num2 + 1):
            div2.append(num2 / i)

        divisor = int(max(list(set(div1).intersection(set(div2)))))
        user_answer = input('Your answer: ')

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f'{user_answer} is wrong answer.\n'
                  f'Correct answer was {divisor}\n'
                  f'Let\'s try again, {user_name}!')
            break

        if user_answer == divisor:
            print('Correct!')
            right_answer_count += 1
        else:
            print(f"'{user_answer}' is wrong answer;(.\n"
                  f"Correct answer was '{divisor}'.\n"
                  f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
