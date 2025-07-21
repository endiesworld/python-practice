"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

"""

def generate_parentheses(n):
    result = []
    current_state = ''
    left = '('
    right = ')'
    left_count = 0
    right_count = 0

    def backtracking(left_count, right_count, current_state):
        if (len(current_state) == n * 2) :
            result.append(current_state)
            return

        if left_count < n:
            left_count_state = left_count
            left_count += 1
            backtracking(left_count, right_count, current_state + left)
            left_count = left_count_state


        if left_count > right_count :
            right_count_state = right_count
            right_count += 1
            backtracking(left_count, right_count, current_state + right)
            right_count = right_count_state

    backtracking(left_count, right_count, current_state)
    return result


if __name__ == "__main__":
    n = 2
    print("Generating parentheses for n =", n)
    combinations = generate_parentheses(n)
    print("All combinations of well-formed parentheses:", combinations)