import sys
input = sys.stdin.readline


def main(is_max: bool, cal: int, cur: int, step: int, ops: list) -> None:
    if is_max:
        if memo.get(cur, _min) < cal:
            memo[cur] = cal
        else:
            return
    else:
        if cal < memo.get(cur, _max):
            memo[cur] = cal
        else:
            return

    for i in range(4):
        if not ops[i]:
            continue
        ops[i] -= 1
        main(is_max, calc(i,cal,arr[step]), cur+(10**i), step+1, ops)
        ops[i] += 1
    return


def calc(_type, x, y):
    if _type == 0:
        return x+y
    if _type == 1:
        return x-y
    if _type == 2:
        return x*y
    return x // y if 0 <= x else -((-x) // y)


if __name__ == '__main__':
    _max = sys.maxsize
    _min = -_max

    N = int(input()) - 1
    start, *arr = map(int, input().split())
    ops = list(map(int, input().split()))

    final = 0
    unit = 1
    for i in range(4):
        final += ops[i] * unit
        unit *= 10

    memo = {}
    main(True, start, 0, 0, ops)
    print(memo[final])
    memo = {}
    main(False, start, 0, 0, ops)
    print(memo[final])
