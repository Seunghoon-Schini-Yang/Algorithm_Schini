def solution(x, y, n):
    def _next(z):
        yield z + n
        yield z * 2
        yield z * 3
        
        
    if x == y: return 0

    memo = [False] * y
    cnt = 0
    que = [x]
    while que:
        tmp = []
        cnt += 1
        for q in que:
            for qq in _next(q):
                if qq == y:  return cnt
                if y < qq or memo[qq]:  continue
                memo[qq] = True
                tmp.append(qq)
        que = tmp
    return -1
