def generate_fibonacci(n):
    fib_series = [0, 1]  

    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)

    return fib_series


user_input = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = generate_fibonacci(user_input)
print(f"Fibonacci Sequence (First {user_input} numbers): {fibonacci_sequence}")
