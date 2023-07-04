from itertools import accumulate


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    honey = list(accumulate(arr))
    rmaxy = max(((honey[-1]-honey[i])<<1) - honey[0] + honey[i-1] for i in range(1, N-1))
    lmaxy = max(honey[-2] - honey[i] + (honey[i-1]<<1) for i in range(1, N-1))
    tmp = honey[-2] - honey[0]
    cmaxy = max(tmp + arr[i] for i in range(1, N-1))
    print(max(rmaxy, cmaxy, lmaxy))
