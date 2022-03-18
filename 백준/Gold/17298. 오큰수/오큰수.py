import sys
input = sys.stdin.readline

def solution(n: int) -> int:
    stack = [0]
    seq = tuple(map(int, input().split()))
    answer = ['-1'] * n

    for i in range(1, n):
        while stack and seq[stack[-1]] < seq[i]:
            answer[stack.pop()] = str(seq[i])
        stack.append(i)

    return ' '.join(answer)


print(solution(int(input())))
