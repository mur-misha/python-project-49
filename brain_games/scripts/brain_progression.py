from brain_games.common_func import welcome_user
import random


def main():
    progression()

def progression():
    user_name = welcome_user()
    print('What number is missing in the progression?')
    right_answer = 0
    while right_answer < 3:
        num1 = random.randint(1, 100)
        step = random.randint(2, 10)

        random_list = [num1 + step * i for i in range(10)]

        rnd_index = random.randint(0, 7)
        rnd_num = random_list[rnd_index]
        random_list[rnd_index] = '...'

        print(f"Question: {' '.join(map(str, random_list))}")
        answer = int(input())

        if answer == rnd_num:
            print(f"Your answer: {answer}")
            print(f'Correct')
            right_answer += 1
        else:
            print(f"Your answer: {answer}")
            print(f"'{answer}' is wrong answer ;(. Correct answer was {rnd_num}\nLet's try again, {user_name}!")
            break

    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()

