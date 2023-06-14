import sys
input = sys.stdin.readline
from collections import deque, defaultdict


if __name__ == '__main__':
    N, K = map(int, input().split())
    q = deque()
    rem = defaultdict(int)
    pairs = 0
    for _ in range(K):
        x = len(input().rstrip())
        pairs += rem[x]
        rem[x] += 1
        q.append(x)
    for _ in range(N-K):
        x = len(input().rstrip())
        pairs += rem[x]
        rem[x] += 1
        q.append(x)
        rem[q.popleft()] -= 1
    print(pairs)
