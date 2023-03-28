N, M = map(int, input().split())
basket = [i for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    basket[a], basket[b] = basket[b], basket[a]
print(*basket[1:])