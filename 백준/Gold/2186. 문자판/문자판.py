import sys
input = sys.stdin.readline
from collections import defaultdict


class KeyBoard():
    def __init__(self, N, M, K):
        board = [input().rstrip() for _ in range(N)]
        d = defaultdict(list)
        for n in range(N):
            for m in range(M):
                d[board[n][m]].append((n, m))
        word = input().rstrip()
        cur = {loc: 1 for loc in d[word[0]]}
        dn, dm = (1, -1, 0, 0), (0, 0, 1, -1)
        for char in word[1:]:
            tmp = defaultdict(int)
            for (n, m), cnt in cur.items():
                for i in range(4):
                    tn, tm = n, m
                    for _ in range(K):
                        tn += dn[i]
                        tm += dm[i]
                        if 0 <= tn < N and 0 <= tm < M:
                            if board[tn][tm] != char:
                                continue
                            tmp[(tn, tm)] += cnt
                        else:
                            break
            cur = tmp
            
        self.cases = sum(cur.values())


if __name__ == '__main__':
    kbd = KeyBoard(*map(int, input().split()))
    print(kbd.cases)
