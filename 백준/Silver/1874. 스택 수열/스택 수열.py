import sys
input = sys.stdin.readline

def solution(n: int):
    stack = list()
    p_n, i = 0, 0
    answer = str()
    for _ in range(n):
        if p_n < (c_n := int(input())):
            while i < c_n:
                i += 1
                stack.append(i)
                answer += '+\n'
            answer += '-\n'
            p_n = stack.pop()

        else:
            if c_n == (p_n := stack.pop()):
                answer += '-\n'
            else:
                return 'NO'

    return answer


print(solution(int(input())))
