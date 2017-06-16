"""Description from karan/Projects:
    Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
"""

def fib(x):
    count = 0
    a, b = 0, 1
    while count <= x:
        a, b = b, a + b
        count += 1
    return a
