import sys
sys.setrecursionlimit(pow(10, 9))
input = sys.stdin.readline


def add_child(parent: int, child: int) -> None:
    graph[- int(guess[parent]) * c_map[guess[parent+1]]].append(int(guess[child]) * c_map[guess[child+1]])


def dfs(node: int) -> int:
    global id, scc_i
    rank[node] = id_memo = id
    stack.append(node)
    id += 1

    for cn in graph[node]:
        if not rank[cn]:
            rank[node] = min(rank[node], dfs(cn))
        elif not finished[cn]:
            rank[node] = min(rank[node], rank[cn])

    if rank[node] == id_memo:
        while True:
            cur = stack.pop()
            finished[cur] = True
            scc_mark[cur] = scc_i
            if node == cur:
                break
        scc_i += 1

    return rank[node]


if __name__ == '__main__':
    k, n = map(int, input().split())
    graph = [[] for _ in range(2*k+1)]
    c_map = {'B': 1, 'R': -1}
    for _ in range(n):
        guess = input().split()
        add_child(0, 2); add_child(0, 4)
        add_child(2, 0); add_child(2, 4)
        add_child(4, 0); add_child(4, 2)

    finished = [False]*(2*k+1)
    finished[0] = True
    rank = [0]*(2*k+1)
    stack = list()

    scc_mark = [0]*(2*k+1)
    id = scc_i = 1

    for i in range(-k, k+1):
        if not finished[i]:
            dfs(i)

    colors = list()
    for i in range(1, k+1):
        if scc_mark[i] == scc_mark[-i]:
            print(-1)
            exit()
        elif scc_mark[i] < scc_mark[-i]:
            colors.append('B')
        else:
            colors.append('R')
    print(''.join(colors))
