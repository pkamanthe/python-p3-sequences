#!/usr/bin/env python3

def print_fibonacci(n):
    if n <= 0:
        print("[]")  
        return
    elif n == 1:
        print("[0]")  
        return

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    print(fib_sequence)
