import sys
from utils.args import get_argument, get_integer_argument
from providers.fib import fib
from providers.factorial import factorial

def main(argv):
    method = get_argument(argv, 0)
    if method == "fib":
        fib(get_integer_argument(argv, 1))
    elif method == "fac":
        factorial(get_integer_argument(argv, 1))
    else:
        print("The method is not valid")

if __name__ == "__main__":
    main(sys.argv[1:])
