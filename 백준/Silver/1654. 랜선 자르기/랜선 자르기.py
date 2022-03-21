import sys
input = sys.stdin.readline

def solution(n: int, k: int) -> int:
    lans = [int(input()) for _ in range(n)]
    cnt = lambda thres: sum(map(lambda x: x // thres, lans))
    top, bottom = max(lans), 1
    while bottom <= top:
        if cnt((mid := (top + bottom) // 2)) < k:
            top = mid - 1
        else:
            bottom = mid + 1
    
    return top


print(solution(*map(int, input().split())))
