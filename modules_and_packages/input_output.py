import re

print(
    f'***This code is running directly in the input_output.py file with module name module is {__name__}***')


def welcome_message():
    print('Hello Emmanuel, welcome to pyhton')


def string_char_counter(arg, char):
    print(
        f"There are {str(arg).lower().count(str(char).lower())} of '{char}' in the {arg} ")
    return None


def keyboard_input_str(user_message='Type any message'):
    format_user_message = user_message + '? '
    user_input = input(format_user_message)
    return user_input

# Only interger input


def keyboard_input_int(user_message='Enter only whole numbers'):
    format_user_message = '{}: '.format(user_message)
    request_input = True

    while(request_input):
        user_input = input(format_user_message)

        # [^ 0-9] means any non-digit character.
        pattern = '[^0-9]'
        check_input = re.search(pattern, user_input)

        if not check_input:
            request_input = False
        else:
            format_user_message = 'Please enter only integers: '

    user_input = int(user_input)

    return user_input


# Any number type input
def keyboard_input(user_message='Enter only Decimal or whole numbers'):
    format_user_message = '{}: '.format(user_message)
    request_input = True

    while(request_input):
        user_input = input(format_user_message)

        # [^0-9\.] means any non-digit character that is not '.'
        pattern = '[^0-9\.]'
        check_input = re.search(pattern, user_input)

        if not check_input:
            request_input = False
        else:
            format_user_message = 'Enter only Decimal or whole numbers: '

    user_input = float(user_input)

    return user_input


""" *** OUT PUT SECTION *** """

# word = keyboard_input_str('Enter the any word')
# char = keyboard_input_str('Enter the character you want to count')
# string_char_counter(word, char)


def close_message():
    number = keyboard_input('Enter a number')
    print('Inputed value: ', number)
