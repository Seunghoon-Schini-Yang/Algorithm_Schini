def main(N: int, K: int) -> int:
    if K <= N:
        return N - K
    memo = [False] * K
    memo[N] = True
    que = [N]
    cnt, cur = 0, K
    while cnt < cur:
        tmp = []
        for q in que:
            cq = q << 1
            while cq < K and not memo[cq]:
                memo[cq] = True
                tmp.append(cq)
                cq <<= 1
            if K <= cq:
                cur = min(cur, cnt + cq - K)
        if cur == cnt:
            return cnt
        
        que += tmp
        tmp = []
        cnt += 1
        for q in que:
            if q+1 == K:
                return cnt
            if not memo[q+1]:
                memo[q+1] = True
                tmp.append(q+1)
            if 1 < q and not memo[q-1]:
                memo[q-1] = True
                tmp.append(q-1)
        que = tmp
    return cnt


if __name__ == '__main__':
    answer = main(*map(int, input().split()))
    print(answer)
