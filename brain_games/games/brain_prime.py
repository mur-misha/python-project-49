#!/usr/bin/env python3

from brain_games.scripts.common_func import welcome_user
import random


def main():
    game()


def is_simple(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def game():
    answer_count = 0
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while answer_count < 3:
        num = random.randint(2, 100)
        print(f'Question: {num}')
        user_answer = input('Your answer: ')

        if user_answer == is_simple(num):
            print('Correct!')
            answer_count += 1
        elif user_answer != is_simple(num):
            print(f"{user_answer} is wrong answer.\n"
                  f"Correct answer was '{is_simple(num)}'\n"
                  f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
