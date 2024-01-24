# Task: Write a program to print the first n numbers of a Fibonacci sequence

def get_fibonacci_sequence(length: int):
    if length >= 0:
        fibonacci = [0, 1]
        for n in range(length - 2):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
        return fibonacci[0:length]


assert get_fibonacci_sequence(0) == []
assert get_fibonacci_sequence(1) == [0]
assert get_fibonacci_sequence(2) == [0, 1]
assert get_fibonacci_sequence(11) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
assert get_fibonacci_sequence(-5) is None
