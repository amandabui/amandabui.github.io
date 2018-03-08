def get_item(lst, i):
	"""
	>>> a = Link(1, Link(6, Link(7)))
	>>> get_item(a, 1)
	6
	"""
	return 

def sum_nums(lnk):
	"""
	>>> a = Link.empty
	>>> a = Link(1, Link(6, Link(7)))
	>>> sum_nums(a)
	14
	"""
	sum = 0 
	while lnk is not Link.empty:
		x = lnk.first
		sum += x  
		lnk = lnk.rest 
	return sum
	## recursive solution 
	if lnk is Link.empty:
		return 0 
	return lnk.first + sum_nums(lnk.rest) 

def multiply_lnks(lst_of_lnks):
	"""
	>>> a = Link(2, Link(3, Link(5)))
	>>> b = Link(6, Link(4, Link(2)))
	>>> c = Link(4, Link(1, Link(0, Link(2))))
	>>> p = multiply_lnks([a, b, c])
	>>> p.first
	48
	>>> p.rest.first
	12
	>>> p.rest.rest.rest
	()
	"""
	product = 1 
	#### lst_of_lnks = [Link.empty, Link.empty, Link(2)]
	for lnk in lst_of_lnks:
		if lnk is Link.empty:
			return Link.empty
		product *= lnk.first
	rest_of_lnks = [lnk.rest for lnk in lst_of_lnks] 
	new_lnk = Link(product, multiply_lnks(rest_of_lnks))
	return new_lnk 

def remove_duplicates(lnk):
	"""
	>>> lnk = Link(1, Link(1, Link(1, Link(5))))
	>>> unique = remove_duplicates(lnk)
	>>> len(unique)
	2
	>>> len(lnk)
	2
	"""
	if lnk is Link.empty or lnk.rest is Link.empty:
		return lnk 
	if lnk.first == lnk.second:
		lnk.rest = lnk.rest.rest
		remove_duplicates(lnk) 
		return lnk 
	remove_duplicates(lnk.rest)
	return lnk

def even_weighted(lst):
	"""
	>>> x = [1, 2, 3, 4, 5, 6]
	>>> even_weighted(x)
	[0, 6, 20]
	"""
	return [...]

def quicksort_list(lst):
	"""
	>>> quicksort_list([3, 1, 4])
	[1, 3, 4]
	"""
	if ___________:
		__________________
	pivot = lst[0]
	less = __________________
	greater = __________________
	return __________________

def eval_tree(tree):
	""" Evaluates an expression tree with 
	functions as the root.
	>>> eval_tree(tree(1))
	1
	>>> expr = tree('*', [tree(2), tree(3)])
	>>> eval_tree(expr)
	6
	>>> eval_tree(tree('+', [expr, tree(4), tree(5)]))
	15
	"""
	if is_leaf(tree):
		return label(tree) 
	args = [eval_tree(branch) for branch in branches(t)]
	if label(tree) == '*':
		return prod(args)
	else:
		return sum(args)




