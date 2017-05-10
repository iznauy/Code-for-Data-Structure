# if we use a list contained 3 elements as BinTree:
# so, we can definate some useful methods
def BinTree(data, left=None, right=None):
    return [data, left, right]

def is_empty_BinTree(btree):
    return btree is None

def root(btree):
    return btree[0]

def left(btree):
    return btree[1]

def right(btree):
    return btree[2]

def set_root(btree, data):
    btree[0] = data

def set_left(btree, left):
    btree[1] = left

def set_right(btree, right):
    btree[2] = right

class UnvaildBinTree(ValueError):
    pass

# basic bin tree
class BasicBinTree(object):
    def __init__(self, data, left=None, right=None):
        if left is not None and not isinstance(left, BasicBinTree):
            raise UnvaildBinTree("left tree must be BinTree!")
        if right is not None and not isinstance(right, BasicBinTree):
            raise UnvaildBinTree("right tree must be BinTree!")
        self._tree = [data, left, right]

    def is_empty(btree):
        return btree is None

    def num_nodes(self):
        left_nodes, right_nodes = 0, 0
        if not left:
            left_nodes = self._tree[1].num_nodes()
        if not right:
            right_nodes = self._tree[2].num_nodes()
        return left_nodes + right_nodes + 1

    def data(self):
        return self._tree[0]

    def left(self):
        return self._tree[1]

    def right(self):
        return self._tree[2]

    def set_left(self, left):
        if left is not None and not isinstance(left, BasicBinTree):
            raise UnvaildBinTree("left tree must be BinTree!")
        self._tree[1] = left

    def set_right(self, right):
        if right is not None and not isinstance(right, BasicBinTree):
            raise UnvaildBinTree("right tree must be BinTree!")
        self._tree[2] = right

    def traversal(self):
        if self._tree[1]:
            for data in self._tree[1].traversal():
                yield data
        yield self._tree[0]
        if self._tree[2]:
            for data in self._tree[2].traversal():
                yield data
        return 

    def pre_order_traversal(self):
        yield self._tree[0]
        if self._tree[1]:
            for data in self._tree[1].pre_order_traversal():
                yield data
        if self._tree[2]:
            for data in self._tree[2].pre_order_traversal():
                yield data
        return 


    def post_order_traversal(self):
        if self._tree[1]:
            for data in self._tree[1].post_order_traversal():
                yield data
        if self._tree[2]:
            for data in self._tree[2].post_order_traversal():
                yield data
        yield self._tree[0]
        return 

    def forall(self, op):
        if self._tree[1]:
            self._tree[1].forall(op)
        self._tree[0] = op(self._tree[0])
        if self._tree[2]:
            self._tree[2].forall(op)
        return
    
    def pre_order_forall(self, op):
        self._tree[0] = op(self._tree[0])
        if self._tree[1]:
            self._tree[1].pre_order_forall(op)
        if self._tree[2]:
            self._tree[2].pre_order_forall(op)
        return
    
    def post_order_forall(self, op):
        if self._tree[1]:
            self._tree[1].post_order_forall(op)
        if self._tree[2]:
            self._tree[2].post_order_forall(op)
        self._tree[0] = op(self._tree[0])
        return       
        
