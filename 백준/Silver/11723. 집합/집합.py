import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(n: int) -> None:
    bitmask = [0] * 21
    empty = [0] * 21
    full = [1] * 21
    
    for _ in range(n):
        query, *x = input().split()
        
        if query == 'add':
            bitmask[int(x[0])] = 1
        elif query == 'all':
            bitmask[:] = full
        elif query == 'remove':
            bitmask[int(x[0])] &= 0
        elif query == 'check':
            print('1\n' if bitmask[int(x[0])] else '0\n')
        elif query == 'toggle':
            bitmask[int(x[0])] ^= 1
        else:
            bitmask[:] = empty


sol(int(input()))
