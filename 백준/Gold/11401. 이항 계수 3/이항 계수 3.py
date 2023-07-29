class BiCoeffcient():
    def __init__(self, N, K):
        K = min(N, N-K)
        mod = 1_000_000_007

        cur = 1
        for i in range(1, K+1):
            cur = (cur * i) % mod
        fac_k = cur
        for i in range(K+1, N-K+1):
            cur = (cur * i) % mod
        fac_nk = cur
        for i in range(N-K+1, N+1):
            cur = (cur * i) % mod
        fac_n = cur
        
        mul = (fac_k * fac_nk) % mod
        cur = 1
        k = mod-2
        while k:
            if k&1:
                cur = (cur * mul) % mod
            mul = (mul * mul) % mod
            k >>= 1
        self.answer = (fac_n * cur) % mod


if __name__ == '__main__':
    bincoff = BiCoeffcient(*map(int, input().split()))
    print(bincoff.answer)
