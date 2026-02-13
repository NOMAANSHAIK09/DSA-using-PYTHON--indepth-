def calculate(n):
    if n > 0:
        print(f" input {n}")
        print(f" cal value {calculate(n - 1)}")
        k = n ** 2
        print(f" k value {k}")


calculate(4)
