# kito4972님 풀이 참고

import sys
input = sys.stdin.readline


def main(m: int, n: int) -> bool:
    def union(x: int, y: int) -> None:
        if parents[x] > parents[y]:
            parents[x] = y
        else:
            if parents[x] == parents[y]:
                parents[x] -= 1
            parents[y] = x
    

    def find(node: int) -> int:
        if parents[node] < 0:
            return node
        parents[node] = find(parents[node])
        return parents[node]
    
    
    if m == n == 0:
        return False
    
    parents = [-1] * m
    _light_total = 0
    _light_on = 0

    roads = []
    for _ in range(n):
        x, y, z = map(int, input().split())
        _light_total += z
        roads.append((z, x, y))
    roads.sort(key=lambda x: x[0])

    for z, x, y in roads:
        # find
        x = find(x); y = find(y)
        if x == y:
            continue
        _light_on += z
        # union
        union(x, y)

    print( _light_total - _light_on )
    return True


if __name__ == '__main__':
    while main(*map(int, input().split())):
        pass
