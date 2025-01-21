#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    # Initialize the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    # Generate the sequence up to the desired length
    for i in range(2, length):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])
    # Trim the sequence to the desired length and print it
    print(fibonacci_sequence[:length])

# Example usage
print_fibonacci(9)
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
