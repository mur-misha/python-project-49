#!/usr/bin/env python3
from random import randint
from brain_games.common_func import welcome_user


def main():
    game()


def is_even(random_number):
    return 'yes' if random_number % 2 == 0 else 'no'


def game():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answer_count = 0

    while right_answer_count < 3:
        random_number = randint(1, 50)
        print(f"Question: {random_number}")
        user_answer = input('Your answer: ').lower()

        if is_even(random_number) == user_answer:
            print('Correct!')
            right_answer_count += 1

        elif is_even(random_number) != user_answer:
            print(f"'{user_answer}' is wrong answer ;(.\n"
                  f"Correct answer was {is_even(random_number)}.\n"
                  f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
