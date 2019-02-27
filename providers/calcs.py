def mult(a,b):
    print(calc_mult(a,b))

def calc_mult(a, b):
    if b == 0:
        return 0
    else:
        return a + calc_mult(a,b-1)

def pot(b,n):
    print(calc_pot(b,n))

def calc_pot(b,n):
    if n <= 0:
        return 1
    if n % 2 == 0:
        pot = calc_pot(b, n/2)
        return calc_mult(pot, pot)
    else:
        pot = calc_pot(b, (n-1)/2)
        return calc_mult(calc_mult(pot, pot), b)
