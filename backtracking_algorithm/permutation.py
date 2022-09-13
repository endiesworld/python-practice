
def permutation(string):
    store = ''
    string_len = len(string) - 1
    return _permutation(string, string_len, 0, store)


def _permutation(string, string_len, pos,  store=''):
    if len(string) == 0:
        return print(store)

    for index, char in enumerate(string):
        store = store + char
        holder = string
        string = string[index+1:]
        _permutation(string, string_len, pos, store)
        # string = holder
        # store = store[:-1]
        # print(char + result)
        # string = string[index:]


print(permutation('ABCD'))
