from string import punctuation, digits, ascii_letters
from random import choices, shuffle

LETTERS = ascii_letters
NUMBER = digits
PUNCTUATION = punctuation


def   input_password_length():
    while 1:
        length = input("Enter your password's length >= 8: ")
        if length.isdigit():
            length = int(length)
            if length >= 8:
                break
    return length


def create_random_password(length = 8):
    temp_str = f'{LETTERS}{NUMBER}{PUNCTUATION}'
    temp_str = list(temp_str)
    shuffle(temp_str)
    random_password = "".join(choices(temp_str, k = length))
    return  random_password


def main():
    length = input_password_length()
    password = create_random_password(length)
    print(f'Your random password: {password}')


if __name__ == "__main__":
    main()