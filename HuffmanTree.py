from PrioQueue import PrioQueue
from BinTree import BinTNode

class HTNode(BinTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data

class HuffmanPrioQ(PrioQueue):
    def number(self):
        return len(self._elems)

def HuffmanTree(weights):
    nodes = []
    for w in weights:
        nodes.append(HTNode(w))
    trees = HuffmanPrioQ(nodes)
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()
