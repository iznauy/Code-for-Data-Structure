class PrioQueueError(ValueError):
    pass

# The less the element is, the more priority the element has.
# if we use line-structure to realize PrioQueue, the consumption of enqueue or dequeue will be O(n)
class PrioQue(object):
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        return self._elems.pop()

    def enqueque(self, e): # O(n)
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)


# But we can use tree-structures to realize PrioQueue, which consumption
# of enqueue will be O(logn), dequeue will be O(logn) and peek will be O(1)
class PrioQueue(object):
    """ Implementing priority queues using heaps
    """
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist: # if not empty
            self.buildheap()

    def buildheap(self):
        end = len(self._elems)
        for i in range(end / 2, -1, -1):
            self.siftdown(self._elems[i], i, end) # really talended! exciting!

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) / 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (i - 1) / 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j] > elems[j+1]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e


# heap sort O(nlogn)
def heap_sort(elems):
    def siftdown(elems, e, begin, end):
        i, j = begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j+1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, j * 2 + 1
        elems[i] = e

    end = len(elems)
    for i in range(end / 2, -1, -1):
        siftdown(elems, elems[i], i, end) # init heap
    for i in range((end - 1), 0, -1):
        e = elems[i]
        elems[i] = elems[0]
        siftdown(elems, e, 0, i)

