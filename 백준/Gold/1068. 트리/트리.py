def main():
    N = int(input())
    ps = map(int, input().split())
    cs = [[] for _ in range(N)]
    out = int(input())

    root = -1
    for c, p in enumerate(ps):
        if p == -1:
            root = c
        elif c != out:
            cs[p].append(c)
    
    if root == out:
        return 0
    
    leafs = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if not cs[node]:
            leafs += 1
        for cn in cs[node]:
            stack.append(cn)
    return leafs


if __name__ == '__main__':
    leafs = main()
    print(leafs)
