import random
import sys

def get_user_input():
    try:
        user_input = int(input('Enter a number between 1 and 10: '))
        if 1 <= user_input <= 10:
            return user_input
        else:
            print('Input out of range. Please try again.')
            return get_user_input()  # Recursively prompt for valid input
    except ValueError:
        print('Invalid input. Please enter a number.')
        return get_user_input()  # Recursively prompt for valid input


def main_loop():
    while True:
        user_number = get_user_input()
        random_number = random.randint(1, 10)
        print(f'You guessed: {user_number}, Random number: {random_number}')
        if user_number == random_number:
            print('Congratulations! You guessed correctly!')
            break
        else:
            print('Try again!')


if __name__ == '__main__':
    main_loop()