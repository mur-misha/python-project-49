#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    game()


def rand():
    rand_number = randint(1, 50)
    return rand_number


def is_even(random_number, user_answer, user_name) -> bool:
    if random_number % 2 == 0:
        if user_answer == 'yes':
            print(f'Your answer is: {user_answer}\nCorrect!')
            return True

        elif user_answer == 'no':
            print(
                f"Your answer is: {user_answer}\n'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {user_name}!""")
            return False

        else:
            print(
                f"Your answer is: {user_answer}\n'{user_answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {user_name}!""")
            return False

    elif random_number % 2 != 0:
        if user_answer == 'no':
            print(f'Your answer is: {user_answer}\nCorrect!')
            return True

        elif user_answer == 'yes':
            print(
                f"Your answer is: {user_answer}\n'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {user_name}!""")
            return False

        else:
            print(
                f"Your answer is: {user_answer}\n'{user_answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {user_name}!""")
            return False

def game():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    right_answer_count = 0
    while right_answer_count < 3:
        random_number = rand()
        print(f"Question: {random_number}")
        user_answer = input().lower()
        if is_even(random_number, user_answer, user_name):
            right_answer_count += 1
        else:
            break
    if right_answer_count == 3:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
