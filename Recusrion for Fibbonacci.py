
"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

def get_fib(position):
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position-1)+get_fib(position-2)

def get_fib1(position):
    first, second = 0, 1
    for fib_pos in range(position - 1):
        first, second = second, first + second
    return second

# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)
