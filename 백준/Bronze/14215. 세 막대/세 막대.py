a, b, c = sorted(map(int, input().split()))
print(a + b + min(a+b-1, c))