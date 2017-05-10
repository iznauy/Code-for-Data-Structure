class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_

class LinkedListUnderflow(ValueError):
    pass

class LList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

    def sort1(self):
        if self._head is None:
            return
        crt = self._head.next
        while crt is not None:
            x = crt.elem
            p = self._head
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            crt.elem = x
            crt = crt.next

    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p
                            
class LList1(LList):
    def __init__(self):
        LList.__init__(self)
        self._rear = None

    def prepend(self, elem):
        if self._head is None:
            LList.prepend(self, elem)
            self._rear = self._head
        else:
            LList.prepend(self, elem)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e

class LCList(object):
    def __init__(self):
        self.__rear = None

    def is_empty(self):
        return self.__rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self.is_empty():
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self.is_empty():
            raise LinkedListUnderflow("in pop")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    def pop_last(self):
        if self.is_empty():
            raise LinkedListUnderflow("in pop_last")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
            return p.elem
        else:
            while p.next is not self._rear:
                p = p.next
            p.next = self._rear.next
            e = self._rear.elem
            self._rear = p
            return e
            
class Josephus(LCList):
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i + 1)
        self.turn(k - 1)
        while noy self.is_empty():
            self.turn(m - 1)
            print(self.pop(), end=('\n' if self.is_empty() else ', '))

