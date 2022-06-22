def binary_search(elements, string_val):

    if len(elements) == 1:
        return 0 if elements[0] == string_val else None

    mid = len(elements) // 2
    if string_val == elements[mid]:
        return mid

    if string_val < elements[mid]:
        return binary_search(elements[:mid], string_val)
    else:
        return mid + binary_search(elements[mid:], string_val)


print(binary_search([1, 2], 2))

print(7.8 // 2)


def fnc(x):
    return 1 if x == 1 else (x * fnc(x-1))


print('The factoria of 5 is: ', fnc(5))
