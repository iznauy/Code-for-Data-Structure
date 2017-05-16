from __future__ import print_function
from MyQueue import SQueue
from Stack import SStack

class BinTNode(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) \
               + count_BinTNodes(t.right)

def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNodes(t.left) \
               + sum_BinTNodes(t.right)

def preorder(t, proc):
    if t is None:
        return None
    proc(t.data)
    preorder(t.left)
    preorder(t.right)

def print_BinTNodes(t):
    if t is None:
        print("^", end='')
        return
    print("(" + str(t.data), end='')
    print_BinTNodes(t.left)
    print_BinTNodes(t.right)
    print(")", end='')

def levelorder(t, proc):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        n = qu.dequeue()
        if n is None:
            continue
        qu.enqueue(n.left)
        qu.enqueue(n.right)
        proc(n.data)

def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()

def midorder_nonrec(t, proc):
    s = SStack()
    d = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.right)
            d.push(t.data)
            t = t.left
        proc(d.pop())
        t = s.pop()

def preorder_elements(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            yield t
            s.push(t.right)
            t = t.left
        t = s.pop()

def midorder_elements(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()
        yield s.pop()

def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left is t.left is not None else t.right
        t = s.pop()
        proc(t.data)
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None

def postorder_elements(t):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right
        t = s.pop()
        yield t.data
        if not s.is_empty() and s.top().left == t:
            t = s.top().right
        else:
            t = None
