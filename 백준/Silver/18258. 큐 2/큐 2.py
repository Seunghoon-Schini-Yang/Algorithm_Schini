import sys
input = sys.stdin.readline

def solution(n: int) -> None:
    q = [0] * n
    left, right = 0, -1

    for _ in range(n):
        if (cmd := input().split())[0] == 'push':
            right += 1
            q[right] = int(cmd[1])
        elif (cmd := cmd[0]) == 'pop':
            if left <= right:
                print(q[left])
                left += 1
            else:
                print(-1)
        elif cmd == 'size':
            print(right - left + 1)
        elif cmd == 'empty':
            if right - left == -1:
                print(1)
            else:
                print(0)
        else:
            if left <= right:
                if cmd == 'front':
                    print(q[left])
                else:
                    print(q[right])
            else:
                print(-1)


solution(int(input()))
