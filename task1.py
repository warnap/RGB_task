import re


def validate_password(password):
    validate = False
    if type(password) is not str:
        password = str(password)

    numbers = [int(char) for char in password]

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            validate = False
            break
        else:
            validate = True

    return validate


def generate_passwords(pass_from, pass_to):
    passwords = range(int(pass_from), int(pass_to) + 1)
    passwords = [str(password) for password in passwords]
    checked_passwords = []
    for password in passwords:
        if re.match(r'(\d)\1', password):
            validate = validate_password(password)
            if validate:
                checked_passwords.append(password)

    return checked_passwords


def get_from_to(input_data):
    input_data = input_data.split('-')
    if input_data[0] > input_data[1]:
        password_from = input_data[1]
        password_to = input_data[0]
    else:
        password_from = input_data[0]
        password_to = input_data[1]

    return password_from, password_to


if __name__ == '__main__':
    print(
        'Welcome in password checker.\n\n' \
        'Please input your passwords range using pattern: nnnnnn-nnnnnn where n is digit: 0-9\n')

    while True:
        data = input('Input range for checking: ')
        if re.match(r"^([\d]{6})([-])([\d]{6})*$", data):
            password_from, password_to = get_from_to(data)
            if password_from != password_to:
                passwords = generate_passwords(password_from, password_to)
                print(len(passwords))
