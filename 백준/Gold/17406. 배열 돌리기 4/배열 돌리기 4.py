import sys
sys.setrecursionlimit(pow(10, 9))
input = sys.stdin.readline
from copy import deepcopy


def get_arr_size(arr: list) -> int:
    return min(sum(row) for row in arr)


def backtrack(arr: list, depth: int) -> None:
    global miny
    if depth == K:
        miny = min(get_arr_size(arr), miny)
        return

    for i in range(K):
        if visited[i]:
            continue
        visited[i] = True
        rotated_arr = rotate(deepcopy(arr), *cals[i])
        backtrack(rotated_arr, depth+1)
        visited[i] = False
    return


def rotate(arr: list, r: int, c: int, s: int) -> list:
    ulr, ulc = r-s-1, c-s-1
    drr, drc = r+s-1, c+s-1
    while ulc < drc and ulr < drr:
        rotate_shell(arr, ulr, ulc, drr, drc)
        ulr += 1; ulc += 1
        drr -= 1; drc -= 1
    return arr


def rotate_shell(arr: list, ulr: int, ulc: int, drr: int, drc: int) -> None:
    ur = arr[ulr][drc]
    arr[ulr][ulc+1:drc+1] = arr[ulr][ulc:drc]
    for row in range(ulr+1, drr+1):
        arr[row-1][ulc] = arr[row][ulc]
    arr[drr][ulc:drc] = arr[drr][ulc+1:drc+1]
    for row in range(drr, ulr, -1):
        arr[row][drc] = arr[row-1][drc]
    arr[ulr+1][drc] = ur
    return


if __name__ == '__main__':
    N,M,K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cals = [tuple(map(int, input().split())) for _ in range(K)]
    visited = [False]*(K)
    miny = 5000
    backtrack(deepcopy(arr), 0)
    print(miny)

