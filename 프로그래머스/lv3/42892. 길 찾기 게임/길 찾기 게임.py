import sys
sys.setrecursionlimit(pow(10, 9))


def solution(nodeinfo):
    def preodr(node):
        if not node:
            return []
        return [node] + preodr(cs[node][0]) + preodr(cs[node][1])
    
    
    def postodr(node):
        if not node:
            return []
        return postodr(cs[node][0]) + postodr(cs[node][1]) + [node]
    
    
    cs = [[0, 0] for _ in range(len(nodeinfo)+1)]
    y_sorted = sorted([(x, y, i) for i, (x, y) in enumerate(nodeinfo, start=1)], key=lambda x: -x[1])
    y_sorted = [i for (_, _, i) in y_sorted]
    nodeinfo = [[]] + nodeinfo
    root = y_sorted[0]
    for i in y_sorted[1:]:
        cur = root
        while True:
            d = 0 if nodeinfo[i][0] < nodeinfo[cur][0] else 1
            if not cs[cur][d]:
                cs[cur][d] = i
                break
            cur = cs[cur][d]
    return [preodr(root), postodr(root)]
