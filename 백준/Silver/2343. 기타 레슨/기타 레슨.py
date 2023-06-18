if __name__ == '__main__':
    N, M = map(int, input().split())
    size = list(map(int, input().split()))
    s, e = max(size), sum(size)
    while s < e:
        m = (s+e)>>1
        cnt = tv = 0
        for v in size:
            if m < tv + v:
                tv = v
                cnt += 1
            else:
                tv += v
        cnt += 1
        if cnt <= M:
            e = m
        else:
            s = m+1
    print(e)
