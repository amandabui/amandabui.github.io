import operator
from functools import reduce

class nil:
    """Represents the special empty pair nil in Scheme."""
    def __repr__(self):
        return 'nil'
    def __len__(self):
        return 0
    def __getitem__(self, i):
        raise IndexError('Index out of range')
    def map(self, fn):
        return nil

nil = nil() # this hides the nil class *forever*s

class Pair:
    """Represents the built-in pair data structure in Scheme."""
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.second)
    def __len__(self):
        return 1 + len(self.second)
    def __getitem__(self, i):
        if i == 0:
            return self.first
        return self.second[i-1]

    def map(self, fn):
        # (Think of a linked list - map will apply the fn to each element in the list by)
        # Here, fn will be applied to every element (.first) in our "link" (our pair). 
        return Pair(fn(self.first), self.second.map(fn))

OPERATORS = {
    '+': lambda *args: sum(args),
    '-': lambda *args: reduce(operator.sub, args),
    '*': lambda *args: reduce(operator.mul, args),
}

def calc_eval(exp):
    """Evaluates a Calculator expression represented as a Pair."""
    print("Evaluating " + str(exp))
    if isinstance(exp, Pair):
        return calc_apply(calc_eval(exp.first),
                          list(exp.second.map(calc_eval)))
    elif exp in OPERATORS:
        return OPERATORS[exp]
    else: # Primitive expression
        return exp

def calc_apply(op, args):
    """Applies an operator to a Pair of arguments."""
    print("Applying " + str(op) +  " to " + str(args))
    return op(*args)

ex = Pair('-', Pair(1, Pair(2, nil)))
p1 = Pair('+', Pair(2, Pair(4, Pair(6, Pair(8, nil)))))
p2 = Pair('+', Pair(2, Pair(Pair('*', Pair(4,Pair(Pair('-', Pair(6, Pair(8, nil))), nil))), nil)))
