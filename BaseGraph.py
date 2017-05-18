class GraphError(ValueError):
    pass

class Graph(object):
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise GraphError('Argument for Graph.')
            self._mat = [mat[i][:] for i in range(vnum)]
            self._unconn = unconn
            self._vnum = vnum

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        return v < 0 or v >= self._vnum

    def add_vertex(self):
        for x in self._mat:
            x.append(unconn)
        self._vnum += 1
        self._mat.append([unconn] * vnum)

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + ' is not a valid vertex')
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + ' is not a valid vertex')
        return self._mat[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + ' or ' + str(vj) + ' is not a valid vertex')
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(len(row)):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return '[\n' + ',\n'.join(map(str, self._mat)) + '\n]'\
               + '\nUnconnected: ' + str(self._unconn)
