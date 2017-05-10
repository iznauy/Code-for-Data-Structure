class StackUnderflow(ValueError):
    pass

class SStack(object):
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def push(self, elem):
        self._elems.append(elem)

    def top(self):
        if self.is_empty():
            raise StackUnderflow('in SStack.top()')
        return self._elems[-1]

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('in SStack.pop()')
        return self._elems.pop()

class LNode(object):
    def __init__(self, elem, _next=None):
        self.elem = elem
        self.next = _next

class LStack(object):
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top == None

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def top(self):
        if self.is_empty():
            raise StackUnderflow('in LStack.top()')
        return self._top.elem

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('in LStack.pop()')
        p = self._top
        self._top = p.next
        return p.elem

def check_parens(text):
    parens = "{}[]()"
    oepn_parens = "{[("
    opposite = {')':'(', ']':'[', '}':'{'}

    def parentheses(text):
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.is_empty() or st.pop() != opposite[pr]:
            print 'Unmatching is found at', i, 'for', pr
            return False

    if st.is_empty():
        print 'All parentheses are correctly matched.'
        return True
    else:
        print 'Some parentheses are not matched by others'
        return False

class ESStack(SStack):
    def depth(self):
        return len(self._elems)

def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())

def suf_exp_evaluator(exp):
    operators = "+-*/"
    st = ESStack()

    for x in exp:
        if x not in operators:
            st.push(int(x) * 1.0)
            continue

        if st.depth() < 2:
            raise SyntaxError("Shorts of operand(s).")
        a = st.pop()
        b = st.pop()

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        else:
            break

        st.push(c)

    if st.depth() == 1:
        return st.pop()
    else:
        raise SyntaxError('Extra operand(s).')


priority = {"(":1, "+":3, "-":3, "*":5, "/":5}
infix_operators = "+-*/()"

def trans_infix_suffix(line):

    
    st = SStack()
    exp = []

    for x in tokens(line):
        if x not in infix_operators:
            exp.append(x)
        elif st.is_empty() or x == '(':
            st.push(x)
        elif x ==')':
            while not st.is_empty() and st.top() != '(':
                exp.append(st.pop())
            if st.is_empty():
                raise SyntaxError("Missing '('.")
            st.pop()
        else:
            while not st.is_empty() and priority[st.top()] >= priority[x]:
                exp.append(st.pop())
            st.push(x)

    while not st.is_empty():
        if st.top() == '(':
            raise SyntaxError("Missing ')'.")
        exp.append(st.pop())

    return exp

def tokens(line):
    i, llen = 0, len(line)
    while i < llen:
        while i < llen and line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:
            yield line[i]
            i += 1
            continue

        j = i + 1
        while j < llen and not line[j].isspace() and line[j] not in infix_operators:
            if (line[j] == 'e' or line[j] == 'E') and j + 1 < llen and line[j+1] == '-':
                j += 1
            j += 1
        yield line[i:j]
        i = j
                
