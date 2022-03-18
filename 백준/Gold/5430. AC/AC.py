from collections import deque
import sys
input = sys.stdin.readline

def solution(n: int) -> None:
    for _ in range(n):
        cmd = input().rstrip()
        input()
        if len((dq := input().rstrip())) == 2:
            dq = deque([])
        else:
            dq = deque(map(int, dq[1:-1].split(',')))
        r_times, e_check = 0, 1

        for char in cmd:
            if char == 'R':
                r_times = not r_times
            else:
                if dq:
                    if r_times:
                        dq.pop()
                    else:
                        dq.popleft()
                else:
                    e_check = 0
                    print('error')
                    break
        
        if e_check:
            if r_times:
                dq.reverse()
        
            if dq:
                print('[' + ','.join(str(list(dq))[1:-1].split(', ')) + ']')
            else:
                print(list(dq))


solution(int(input()))
