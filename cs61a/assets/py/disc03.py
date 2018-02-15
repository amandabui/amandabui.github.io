def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)
# </block adt>

# <block print-tree>
def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.
    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
# </block print-tree>

# <block copy-tree>
def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.
    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def tree_max(t):
	"""Return the max of a tree."""
	# if is_leaf(t):
	# 	return label(t)
	# max_labels = [label(t)] 
	# for branch in branches(t):
	# 	max_labels += [tree_max(branch)]
	# return max(max_labels)

	return max([label(t)] + [tree_max(branch) for branch in branches(t)])

def height(t):
	"""Return the height of a tree - the depth of the lowest leaf."""
	if is_leaf(t):
		return 0 
	heights_of_subtrees = [] 
	for branch in branches(t):
		heights_of_subtrees += [height(branch)]
	return 1 + max(heights_of_subtrees)


	##### list comprehension
	if is_leaf(t):
		return 0 
	return 1 + max([height(branch) for branch in branches(t)])

def square_tree(t):
	"""Return a NEW!!!! tree with the square of every element in t"""
	if is_leaf(t):
		return tree(label(t)**2)
	squared_branches = [] 
	for branch in branches(t):
		squared_branches += [square_tree(branch)]
	return tree(label(t)**2, squared_branches)


	### list comprehension
	return tree(label(t)**2, [square_tree(branch) for branch in branches(t)])
