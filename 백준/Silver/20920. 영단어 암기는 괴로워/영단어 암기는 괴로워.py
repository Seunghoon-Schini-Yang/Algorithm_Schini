import sys
input = sys.stdin.readline


N, M = map(int, input().split())
memo = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) < M:
        continue
    memo[word] = memo.get(word, 0) + 1

memo = [(word, cnt) for word, cnt in memo.items()]
memo.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
memo = [word for word, _ in memo]
print('\n'.join(memo))
