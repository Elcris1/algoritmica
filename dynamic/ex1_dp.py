# (Fibonacci Sequence:) Compute the nth Fibonacci number efficiently using dynamic programming to avoid redundant calculations.

# 0 1 1 2 3 5 8 13

def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_dp(n, array):
    if n <= 1:
        return n
    if array[n] != -1:
        return array[n]

    array[n] = fibonacci_dp(n-1, array) + fibonacci_dp(n-2, array)
    return array[n]

def fibonacci_profesor(n):
    memo = [0, 1]
    for i in range(2, n+1):
        memo.append(memo[i - 1] + memo[i - 2])
    return memo[n]


print(fibonacci_profesor(50))