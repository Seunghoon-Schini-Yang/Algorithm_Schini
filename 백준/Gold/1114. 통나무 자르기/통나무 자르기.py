class Log():
    def __init__(self, L, K, C):
        acc = sorted(set(map(int, input().split())))
        while acc and acc[-1] == L:
            acc.pop()
        acc.append(L)
        arr = acc[:]
        K = len(arr)
        s, e = arr[0], L
        for i in range(K-1):
            arr[i+1] = acc[i+1] - acc[i]
            s = arr[i+1] if arr[i+1] > s else s
        arr = arr[::-1]
        C += 1
        if C < K:
            while s < e:
                m = (s+e)>>1
                pack = i = cur = 0
                while i < K and pack < C:
                    while i < K and cur+arr[i] <= m:
                        cur += arr[i]
                        i += 1
                    pack += 1
                    cur = 0
                if i < K:
                    s = m+1
                else:
                    e = m
        acc = arr[:]
        for i in range(K-1):
            acc[i+1] = acc[i] + arr[i+1]
        i = cur = pack = 0
        while i < K and pack < C-1:
            while i < K and cur+arr[i] <= s:
                cur += arr[i]
                i += 1
            pack += 1
            cur = 0
        loc = arr[-1] if i == K else L-acc[i-1]
        self.answer = (s, loc)


if __name__ == '__main__':
    log = Log(*map(int, input().split()))
    print(*log.answer)
