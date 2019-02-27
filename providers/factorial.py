def factorial(n):
    print(calc_factorial(n))

def calc_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calc_factorial(n-1)
