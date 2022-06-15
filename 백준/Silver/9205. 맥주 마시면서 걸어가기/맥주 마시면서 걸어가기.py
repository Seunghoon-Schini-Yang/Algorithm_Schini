import sys
input = sys.stdin.readline
from collections import deque


def sol(n: int) -> int:
    que = deque([tuple(map(int, input().split()))])
    visited = {que[0]}
    stores = [tuple(map(int, input().split())) for _ in range(n+1)]
    gx, gy = stores[-1]
    stores.sort()  # nlogn

    while que:
        x,y = que.popleft()
        if x==gx and y==gy:
            return 'happy'
        
        for nx,ny in stores[bisect_left(stores, 0, x-1000):bisect_right(stores, 0, x+1000)]:
            if (nx,ny) not in visited and abs(x-nx)+abs(y-ny) <= 1000:
                visited.add((nx,ny))
                que.append((nx,ny))

    return 'sad'


def bisect_left(arr: list, idx: int, x: int) -> int:
    lo = 0; hi = len(arr)-1
    if arr[hi][idx] < x:
        return hi+1
    
    while lo < hi:
        mid = (lo+hi)>>1
        if arr[mid][idx] >= x:
            hi = mid
        else:
            lo = mid+1
    return lo


def bisect_right(arr: list, idx: int, x: int) -> int:
    lo = 0; hi = len(arr)-1
    if arr[hi][idx] <= x:
        return hi+1
    
    while lo < hi:
        mid = (lo+hi)>>1
        if arr[mid][idx] <= x:
            lo = mid+1
        else:
            hi = mid
    return lo


if __name__ == '__main__':
    print('\n'.join(sol(int(input())) for _ in range(int(input()))))
