import sys
INF = sys.maxsize


def solution(numbers):
    typing = [(divmod(i-1, 3)) for i in range(10)]
    typing[0] = (3, 1)
    ds = [[1] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(i+1, 10):
            x, y = (abs(x-y) for x, y in zip(typing[i], typing[j]))
            ds[i][j] = ds[j][i] = min(x, y) * 3 + abs(x-y) * 2

    que = {(4, 6): 0}
    for num in map(int, numbers):
        tmp = {}
        for (l, r), v in que.items():
            if l == num or r == num:
                if v + 1 < tmp.get((l, r), INF):
                    tmp[(l, r)] = v + 1
                continue
            
            _key = (num, r) if num < r else (r, num)
            if v + ds[l][num] < tmp.get(_key, INF):
                tmp[_key] = v + ds[l][num]
            _key = (num, l) if num < l else (l, num)
            if v + ds[r][num] < tmp.get(_key, INF):
                tmp[_key] = v + ds[r][num]         
        que = tmp
    return min(que.values())
