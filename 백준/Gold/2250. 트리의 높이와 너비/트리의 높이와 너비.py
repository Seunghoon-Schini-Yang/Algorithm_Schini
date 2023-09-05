import sys
input = sys.stdin.readline


class Tree():
    def __init__(self, N):
        self.tree = [(0, 0) for _ in range(N+1)]
        is_root = [True] * (N+2)
        for _ in range(1, N+1):
            p, l, r = map(int, input().split())
            self.tree[p] = (l, r)
            is_root[l] = is_root[r] = False
        for i in range(1, N+1):
            if is_root[i]:
                root = i
                break
        self.children = [[0, 0] for _ in range(N+1)]
        self.edges = [[10000, -10000] for _ in range(N+1)]
        self._dfs_count(root)
        self._dfs_breadth(root, 1, 0)
        
        widest = [1, 1]
        for i in range(2, N+1):
            cur = self.edges[i][1] - self.edges[i][0] + 1
            if cur < 0:
                break
            if widest[1] < cur:
                widest = [i, cur]
        self.answer = widest

    
    def _dfs_count(self, node):
        cnt = 1
        for i in range(2):
            cur = 0 if self.tree[node][i] == -1 else self._dfs_count(self.tree[node][i])
            self.children[node][i] = cur
            cnt += cur
        return cnt
    

    def _dfs_breadth(self, node, depth, loc):
        if loc < self.edges[depth][0]:
            self.edges[depth][0] = loc
        if loc > self.edges[depth][1]:
            self.edges[depth][1] = loc
        
        for i in range(2):
            cnode = self.tree[node][i]
            if cnode == -1:
                continue
            cloc = loc + (1 if i else -1) * (self.children[cnode][i^1] + 1)
            self._dfs_breadth(cnode, depth+1, cloc)


if __name__ == '__main__':
    tree = Tree(int(input()))
    print(*tree.answer)
