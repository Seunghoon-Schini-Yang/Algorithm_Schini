import sys
input = sys.stdin.readline


n = int(input())
current = set()
for _ in range(n):
    _name, is_enter = input().split()
    if is_enter[0] == 'e':
        current.add(_name)
    else:
        current.discard(_name)
print('\n'.join(sorted(current, reverse=True)))
