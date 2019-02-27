def mult(a,b):
    print(calc_mult(a,b))

def calc_mult(a, b):
    if b == 0:
        return 0
    else:
        return a + calc_mult(a,b-1)
