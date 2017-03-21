import sympy as sp

def case_0_symbols():
    a, b, c = args = tuple(sp.Symbol(arg) for arg in $)
    return args
case_0_symbols.expected = tuple(sp.symbols('a b c'))

cases = (case_0_symbols,)
