class QueueUnderflow(ValueError):
    pass

class SQueue(object):
    def __init__(self, init_len=8):
        self._elem = [0] * init_len
        self._len = init_len
        self._num = 0
        self._head = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if is_empty():
            raise QueueUnderflow
        return self._elem[self._head]

    def dequeue(self):
        if is_empty():
            raise QueueUnderflow
        e = self._elem[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elem[(self._head + self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elem[(self._head + i) % old_len]
        self._elem = new_elems
        self._head = 0
