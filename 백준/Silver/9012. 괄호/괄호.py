import sys
input = sys.stdin.readline

def solution(n: int) -> None:
    for _ in range(n):
        stack = list()
        cont = 0

        for pc in input().rstrip():
            if pc == '(':
                stack.append(pc)
            else:
                if stack:
                    stack.pop()
                else:
                    print('NO')
                    cont = 1
                    break
                    
        if cont:
            continue

        if stack:
            print('NO')
        else:
            print('YES')


solution(int(input()))
