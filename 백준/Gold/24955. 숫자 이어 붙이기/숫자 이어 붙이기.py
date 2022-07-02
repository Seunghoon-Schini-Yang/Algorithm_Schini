import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10,9))


def dfs(p_node: int, node: int) -> str:
    global e

    if node == e:
        return str(gate_nums[node])

    for c_node in roads[node]:
        if c_node != p_node:
            c_res = dfs(node, c_node)
            if c_res:
                return str(gate_nums[node]) + c_res
    return False


if __name__ == '__main__':
    N,Q = map(int, input().split())
    gate_nums = [0] + list(map(int, input().split()))
    roads = [[] for _ in range(N+1)]

    for _ in range(N-1):
        a,b = map(int, input().split())
        roads[a].append(b)
        roads[b].append(a)

    for _ in range(Q):
        s,e = map(int, input().split())
        print(int(dfs(0, s)) % 1_000_000_007)
