import sys
input = sys.stdin.readline
from bisect import bisect_left


def main(N, arr):
    if N == 1:
        print(1)
        return
    
    inc = [0] * N; dec = inc[:]
    imemo = []; dmemo = []
    for i in range(N):
        if (ii := bisect_left(imemo, arr[i])) == len(imemo):
            imemo.append(arr[i])
        else:
            imemo[ii] = arr[i]
        inc[i] = ii
        if (di := bisect_left(dmemo, arr[~i])) == len(dmemo):
            dmemo.append(arr[~i])
        else:
            dmemo[di] = arr[~i]
        dec[i] = di
    
    for i in range(1, N):
        if inc[i] < inc[i-1]:
            inc[i] = inc[i-1]
        if dec[i] < dec[i-1]:
            dec[i] = dec[i-1]

    print( max(inc[i] + dec[N-1-i] for i in range(N)) + 1 )


if __name__ == '__main__':
    main(int(input()), list(map(int, input().split())))
