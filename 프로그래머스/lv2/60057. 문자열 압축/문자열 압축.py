def solution(s):
    miny = n = len(s)
    for thr in range(1, (n>>1)+1):
        acc = 0
        i = thr
        std = s[:i]
        cnt = 1
        while i < n:
            if std == s[i:i+thr]:
                cnt += 1
            else:
                acc += thr if cnt==1 else thr+len(str(cnt))
                std = s[i:i+thr]
                cnt = 1
            i += thr
        acc += len(std) if cnt==1 else thr+len(str(cnt))
        miny = min(miny, acc)
    return miny
