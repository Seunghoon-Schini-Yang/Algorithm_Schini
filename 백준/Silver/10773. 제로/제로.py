import sys
input = sys.stdin.readline

def solution(n: int) -> int:
    stack = list()

    for _ in range(n):
        if (num := int(input())):
            stack.append(num)
        else:
            stack.pop()

    return sum(stack)


print(solution(int(input())))
