import sys
input = sys.stdin.readline

def solution(n: int) -> None:
    front, back = n, n - 1
    ans = list()
    deq = [0] * (2 * n)

    for _ in range(n):
        if (cmd := input().rstrip())[1] == 'u':
            if cmd[5] == 'f':
                front -= 1
                deq[front] = cmd[11:]
            else:
                back += 1
                deq[back] = cmd[10:]
        elif cmd[1] == 'm':
            ans.append('1' if front > back else '0')
        elif cmd[1] == 'i':
            ans.append(str(back - front + 1))
        else:
            if front > back:
                ans.append('-1')
            elif cmd[1] == 'o':
                if cmd[4] == 'f':
                    ans.append(deq[front])
                    front += 1
                else:
                    ans.append(deq[back])
                    back -= 1
            elif cmd[1] == 'r':
                ans.append(deq[front])
            else:
                ans.append(deq[back])

    return '\n'.join(ans)


print(solution(int(input())))
