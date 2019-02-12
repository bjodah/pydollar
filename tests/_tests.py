# here's a dollar sign in a comment $
from collections import OrderedDict

my_evil_values = ('_DOLLAR_SIGN_LITERAL_0_', '_DOLLAR_SIGN_LITERAL_1_')
price = '$42'

def case_0():
    a, b, c = args = $
    return args
case_0.expected = ('a', 'b', 'c')

def case_1():
    hello, world = map(str.capitalize, $)
    return hello, world
case_1.expected = ('Hello', 'World')

def case_2():
    houston, do, you, copy = args = [word.upper() for word in $]
    return ' '.join(args)
case_2.expected = 'HOUSTON DO YOU COPY'

def case_3():
    alpha, beta, gamma = d = OrderedDict([(k, k.upper()) for k in $])
    return d
case_3.expected = {'alpha': 'ALPHA', 'beta': 'BETA', 'gamma': 'GAMMA'}


cases = (case_0, case_1, case_2, case_3, case_4)
