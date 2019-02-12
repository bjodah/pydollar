# here's an exlamation mark in a comment !

my_evil_excl = ('_EXLAMATION_MARK_LITERAL_0_', '_EXLAMATION_MARK_LITERAL_1_')
greeting_excl = 'hello world!'

def case_excl_0():
    spl!str.split, ev!eval, flt!float = ['a b c', '10**3', '1e42']
    return spl, ev, flt

case_excl_0.expected = (['a','b','c'], 1000, 1e42)

cases_excl = (case_excl_0,)
