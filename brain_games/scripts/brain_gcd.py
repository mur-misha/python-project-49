#!/usr/bin/env python3

from brain_games.common_func import welcome_user, random_num


def main():
    brain_gcd()


def brain_gcd():
    user_name = welcome_user()
    right_answer_count = 0
    print('Find the greatest common divisor of given numbers.')

    while right_answer_count < 3:
        a = random_num()
        b = random_num()
        a_div = []
        b_div = []
        print(f'Question: {a} {b}')

        for i in range(1, a + 1):
            a_div.append(a / i)
        for i in range(1, b + 1):
            b_div.append(b / i)

        big_common_div = int(max(list(set(a_div).intersection(set(b_div)))))
        user_answer = int(input("Your answer: "))

        if user_answer == big_common_div:
            print('Correct!')
            right_answer_count += 1
        else:
            print(f"'{user_answer}' is wrong answer;(.\n"
                  f"Correct answer was '{big_common_div}'.\n"
                  f"Let's try again, {user_name}!")
            break
    else:
        print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
