from itertools import permutations as p
from itertools import combinations as c


if __name__ == '__main__':
    N = int(input())
    target = tuple(map(int, input().split()))
    mapping = {seq: 0.0 for seq in p(range(1, N+1))}

    for seq in p(range(1, N+1)):
        acc = ways = 0
        for i, j in c(range(N), 2):
            if seq[i] < seq[j]:
                continue

            seq_l = list(seq)
            seq_l[i], seq_l[j] = seq_l[j], seq_l[i]
            acc += mapping[tuple(seq_l)] + 1
            ways += 1
        
        if ways:
            mapping[seq] = acc / ways
        if seq == target:
            break
    
    print(mapping[target])
