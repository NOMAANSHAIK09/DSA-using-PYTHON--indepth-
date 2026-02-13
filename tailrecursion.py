# when a function call itsefl at the last of function , no statement shold be after that than it is tail recurision 


def calculate(n):
    if n > 0:
        k = n ** 2
        print(k)
        calculate(n - 1)



calculate(4)
