def solution(a: int, b:int, c: int) -> int:
    if b == 1:
        return a % c
    
    now = solution(a, b >> 1, c)
    if b & 1:
        return now * now * a % c
    else:
        return now * now % c


print(solution(*map(int, input().split())))
