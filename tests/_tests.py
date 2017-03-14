
# here's a dollar sign in a comment $

my_evil_values = ('_DOLLAR_SIGN_LITERAL_0_', '_DOLLAR_SIGN_LITERAL_1_')
price = '$42'

def case_1():
    a, b, c = args = $
    return args
case_1.expected = ('a', 'b', 'c')

def case_2():
    hello, world = map(str.capitalize, $)
    return hello, world
case_2.expected = ('Hello', 'World')

def case_3():
    houston, do, you, copy = args = [word.upper() for word in $]
    return ' '.join(args)
case_3.expected = 'HOUSTON DO YOU COPY'

def case_4():
    alpha, beta, gamma = d = {k: k.upper() for k in $}
    return d
case_4.expected = {'alpha': 'ALPHA', 'beta': 'BETA', 'gamma': 'GAMMA'}

cases = (case_1, case_2, case_3, case_4)
