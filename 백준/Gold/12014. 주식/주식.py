import sys
input = sys.stdin.readline
from bisect import bisect_left


class Stock():
    def __init__(self, N, K):
        q = []
        for price in map(int, input().split()):
            idx = bisect_left(q, price)
            if idx == len(q):
                q.append(price)
            else:
                q[idx] = price
        self.is_poss = 1 if K <= len(q) else 0
        

if __name__ == '__main__':
    for i in range(1, int(input())+1):
        print(f'Case #{i}')
        invest = Stock(*map(int, input().split()))
        print(invest.is_poss)
