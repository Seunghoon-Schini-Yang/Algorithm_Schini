if __name__ == '__main__':
    N, K = input().split()
    if len(N) == 1 or (len(N) == 2 and N[1] == '0'):
        print(-1)
        exit()
    K = int(K)
    q = [N]
    n = len(N)

    for _ in range(K):
        tmp = set()
        for s in q:
            cur = list(s)
            for i in range(n-1):
                for j in range(i+1, n):
                    if not i and cur[j] == '0':
                        continue
                    cur[i], cur[j] = cur[j], cur[i]
                    tmp.add(''.join(cur))
                    cur[i], cur[j] = cur[j], cur[i]
        q = tmp
    print(max(map(int, q)))
