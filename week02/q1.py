def getFibonacciNumbers(n):
    """Returns a list of Fibonacci numbers less than or equal to n."""
    if n < 0:
        return []  
    
    fib_numbers = [0, 1]  
    while True:
        next_fib = fib_numbers[-1] + fib_numbers[-2]
        if next_fib > n:
            break
        fib_numbers.append(next_fib)
    
    return fib_numbers if n >= 1 else [0]

print(getFibonacciNumbers(10))