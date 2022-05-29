print('Hello Emmanuel, welcome to pyhton')


def string_char_counter(arg, char):
    print(
        f"There are {str(arg).lower().count(str(char).lower())} of '{char}' in the {arg} ")
    return None


def keyboard_input_str(user_message='Type any message'):
    format_user_message = user_message + '? '
    user_input = input(format_user_message)
    return user_input


def keyboard_input_int(user_message='Type any message'):
    format_user_message = user_message + ': '
    user_input = input(format_user_message)
    user_input = float((user_input))
    if (user_input).is_integer():
        user_input = int(user_input)
    return user_input


""" *** OUT PUT SECTION *** """

# word = keyboard_input_str('Enter the any word')
# char = keyboard_input_str('Enter the character you want to count')
# string_char_counter(word, char)

print(int(5/2))

number = keyboard_input_int('Enter a number')
print('Inputed value: ', number)
