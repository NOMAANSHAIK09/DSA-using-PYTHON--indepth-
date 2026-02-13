# when a function call itself first means after base condition , no other statement before it

def calculate(n):
    if n > 0:
       
        print(calculate(n - 1))
        k = n ** 2
        print(k)


calculate(4)

