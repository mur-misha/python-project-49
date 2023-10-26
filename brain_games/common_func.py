import prompt
from random import randint

def welcome_user() -> str:
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def random_num():
    return randint(1, 50)
