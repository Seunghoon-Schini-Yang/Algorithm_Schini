import sys
input = sys.stdin.readline


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        selected = [0] + list(map(int, input().split()))
        visited = [False]*(n+1)
        cnt = 0

        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                cur_cycle = {i}
                cur = selected[i]

                while True:
                    if not visited[cur]:
                        visited[cur] = True
                        cur_cycle.add(cur)
                        cur = selected[cur]
                    elif cur in cur_cycle:
                        cur_cycle.remove(cur)
                        cur = selected[cur]
                    else:
                        cnt += len(cur_cycle)
                        break
    
        print(cnt)
    