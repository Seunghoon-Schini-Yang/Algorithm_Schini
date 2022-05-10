import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(n: int) -> None:
    bitmask = [0] * 21
    empty = [0] * 21
    full = [1] * 21
    
    for _ in range(n):
        query = input().split()
        
        if query[0] == 'add':
            bitmask[int(query[1])] = 1
        elif query[0] == 'all':
            bitmask[:] = full
        elif query[0] == 'remove':
            bitmask[int(query[1])] &= 0
        elif query[0] == 'check':
            print('1\n' if bitmask[int(query[1])] else '0\n')
        elif query[0] == 'toggle':
            bitmask[int(query[1])] ^= 1
        else:
            bitmask[:] = empty


sol(int(input()))
