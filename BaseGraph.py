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
            x.append(self._unconn)
        self._vnum += 1
        self._mat.append([self._unconn] * self._vnum)
        return self._vnum - 1

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


class DirectedGraph(Graph): # orientedGraph
    def __init__(self, mat=[], unconn=0):
        self._vnum = len(mat)
        for x in mat:
            if len(x) != self._vnum:
                raise GraphError('Argument for DirectedGraph')
            self._mat = [Graph._out_edges(mat[i], unconn) for i in range(self._vnum)]
            self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + ' is not a valid vertex.')
        return self._mat[vi]

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + ' is not a valid vertex')
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError('Cannot add edge to empty graph.')
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + ' is not a valid vertex')
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))


class UndirectedGraph(DirectedGraph):
    def __init__(self, mat=[], unconn=0):
        self._vnum = len(mat)
        for x in mat:
            if len(x) != self._vnum:
                raise GraphError('Argument for Graph')
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(self._vnum)]
        self._unconn = unconn
        if not self._valid_matrix(mat):
            raise GraphError('Invalid matrix in UndirectedGraph')

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError('Cannot add edge to empty graph.')
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) + ' is not a valid vertex')
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))
        row = self._mat[vj]
        i = 0
        while i < len(row):
            if row[i][0] == vi:
                self._mat[vj][i] = (vi, val)
                return
            if row[i][0] > vi:
                break
            i += 1
        self._mat[vj].insert(i, (vi, val))

    def _valid_matrix(self, mat):
        for i in range(len(mat)):
            for j in range(i + 1, len(mat)):
                if mat[i][j] != mat[j][i]:
                    return False
        return True
