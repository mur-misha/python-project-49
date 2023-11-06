#!/usr/bin/env python3

from brain_games.scripts.common_func import welcome_user
import random


def main():
    progression()


def progression():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    right_answer = 0

    while right_answer < 3:
        num = random.randint(1, 100)
        step = random.randint(2, 10)

        random_list = [num + step * i for i in range(10)]

        rnd_index = random.randint(0, 9)
        rnd_num = random_list[rnd_index]
        random_list[rnd_index] = '...'

        print(f"Question: {' '.join(map(str, random_list))}")
        answer = input('Your answer: ')
        try:
            answer = int(answer)
        except ValueError:
            print(f'{answer} is wrong answer. Correct answer was {rnd_num}\n'
                  f'Let\'s try again, {user_name}!')
            break
        if answer == rnd_num:
            print("Correct")
            right_answer += 1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {rnd_num}\n"
                  f"Let's try again, {user_name}!")
            break

    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
