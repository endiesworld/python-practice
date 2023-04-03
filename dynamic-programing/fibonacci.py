def fib_1(n):
    result =  1
    if (n == 1) or (n == 2):
        return result
    result = fib(n-1) + fib(n-2)
    return result

# The above function leands to a complexcity of O(2^n). 

# With memoization
def fib_memo(n, memo):
    result = 1
    if memo[n] is not None:
        return memo[n]
    if (n == 1) or (n == 2):
        return result
    result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = result
    return result

def fib(n):
    memo = [None] * (n + 1)
    return fib_memo(n, memo)

print(fib(7))