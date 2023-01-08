import sys
input = sys.stdin.readline


not_handed = {i for i in range(1, 31)}
for _ in range(28):
    not_handed.remove(int(input()))
not_handed = sorted(not_handed)
print(not_handed[0])
print(not_handed[1])
