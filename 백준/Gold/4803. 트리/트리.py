# my
# disjoint set
import sys
input = sys.stdin.readline


def sol() -> None:
    case = 1
    while count_trees(*map(int, input().split()), case):
        case += 1


def count_trees(n: int, m: int, case: int) -> bool:
    if n == m == 0:
        return False


    def find(x: int) -> int:
        if ps[x] < 0:
            return x
        ps[x] = find(ps[x])
        return ps[x]
    

    def union(root_x: int, root_y: int) -> None:
        if ps[root_x] > ps[root_y]:
            ps[root_x] = root_y
        else:
            if ps[root_x] == ps[root_y]:
                ps[root_x] -= 1
            ps[root_y] = root_x


    ps = [-1] * (n+1)
    cycle_root = set()

    for _ in range(m):
        a,b = map(int, input().split())
        root_a = find(a); root_b = find(b)

        if root_a == root_b:
            cycle_root.add(root_a)

        else:
            union(root_a, root_b)

    cnt = 0
    for i in range(1,n+1):
        if ps[i] < 0 and i not in cycle_root:
            cnt += 1
    
    if not cnt:
        print(f'Case {case}: No trees.')
    elif cnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')

    return True

sol()
