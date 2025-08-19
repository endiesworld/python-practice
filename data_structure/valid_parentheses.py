def isValid( s: str) -> bool:
    string_pair = {')': '(', '}': '{', ']': '['}
    stack = []
    close = [')', '}', ']']

    for data in s:
        if (data in string_pair) and (len(stack) > 0):
            last_br = stack.pop()
            if last_br == string_pair[data]:
                continue
            else:
                return False

        elif (data in string_pair) and (len(stack) == 0):
            return False
        else:
            stack.append(data)
            print("Stack after pushing:", stack)
    print("Stack at end:", stack)
    if len(stack) > 0:
        return False

    return True

if __name__ == "__main__":
    s = "()[]{}"
    print(isValid(s))  # Output: True

    # s = "(]"
    # print(isValid(s))  # Output: False

    # s = "([)]"
    # print(isValid(s))  # Output: False

    # s = "{[]}"
    # print(isValid(s))  # Output: True