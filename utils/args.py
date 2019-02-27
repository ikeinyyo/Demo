def get_argument(argv, index):
    return argv[index]

def get_integer_argument(argv, index):
    arg = get_argument(argv, index)
    return int(arg)
