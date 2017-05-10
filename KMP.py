def naive_matching(t, p):
    """navie matching, O(m*n)"""
    m, n = len(p), len(t)
    i, j = 0, 0
    while i < m and j < n:
        if t[j] == p[i]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - i + 1
    if i == m:
        return j - i
    return -1

def matching_kmp(t, p, pnext):
    """KMP match, O(n)"""
    m, n = len(p), len(t)
    i, j = 0, 0
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            i, j = i + 1, j + 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1

def gen_pnext(p):
    """generate the pnext"""
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext

def great_gen_pnext(p):
    """some improve in gen_pnext"""
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]
    return pnext
