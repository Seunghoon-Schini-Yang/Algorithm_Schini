class Spicy():
    def __init__(self, N):
        rem = 1_000_000_007
        peppers = sorted(map(int, input().split()))
        for i in range(1, N):
            peppers[i] = (peppers[i-1]+peppers[i]) % rem
        self._sum_up(N, rem, peppers)
    
    
    def _sum_up(self, N, rem, peppers):
        answer = 0
        double = 1
        for i in range(N-1):
            answer += (peppers[-1] - peppers[i] - peppers[-2-i]) * double
            answer %= rem
            double = (double<<1) % rem
        self.tot_gap = answer


if __name__ == '__main__':
    spicy_comb = Spicy(int(input()))
    print(spicy_comb.tot_gap)
