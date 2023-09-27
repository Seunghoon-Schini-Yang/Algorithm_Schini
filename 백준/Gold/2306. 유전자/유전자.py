class DNA():
    def __init__(self, seq):
        self.seq = seq
        self.n = len(seq)


def main():
    dna = DNA(input())
    memo = [[0] * dna.n for _ in range(dna.n)]
    for d in range(1, dna.n):
        for l in range(dna.n - d):
            r = l+d
            memo[l][r] = max(memo[l][i] + memo[i+1][r] for i in range(l, r))
            if (dna.seq[l] == 'a' and dna.seq[r] == 't') or (dna.seq[l] == 'g' and dna.seq[r] == 'c'):
                memo[l][r] = max(memo[l][r], memo[l+1][r-1] + 2)
    print(memo[0][-1])


if __name__ == '__main__':
    main()
