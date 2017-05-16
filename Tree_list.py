class SubtreeIndexError(ValueError):
    pass

def Tree(data, *substrees):
    return [data].extend(subtrees)

def is_empty_Tree(tree):
    return tree is None

def root(tree):
    return tree[0]

def subtree(tree, i):
    if i < 1 or i >= len(tree):
        raise SubtreeIndexError
    return tree[i]

def set_root(tree, data):
    tree[0] = data

def set_subtree(tree, i, subtree):
    if i < 1 or i >= len(tree):
        raise SubtreeIndexError
    tree[i] = subtree

