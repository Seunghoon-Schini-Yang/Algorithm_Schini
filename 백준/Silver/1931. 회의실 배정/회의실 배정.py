import sys
input = sys.stdin.readline

def solution(n: int) -> int:
    times = [tuple(map(int, input().split())) for _ in range(n)]
    times.sort(key=lambda x: (x[1], x[0]))
    
    std, answer = 0, 0
    for start, end in times:
        if start >= std:
            answer += 1
            std = end
    
    return answer


print(solution(int(input())))
