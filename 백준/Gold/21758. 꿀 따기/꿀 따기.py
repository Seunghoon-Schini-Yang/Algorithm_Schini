from itertools import accumulate


if __name__ == '__main__':
    N = int(input())
    honey = list(accumulate(map(int, input().split())))
    rmaxy = max((honey[-1] - honey[0]) - (honey[i] - honey[i-1]) + (honey[-1] - honey[i]) for i in range(1, N-1))
    lmaxy = max(honey[-2] - (honey[i] - honey[i-1]) + honey[i-1] for i in range(1, N-1))
    cmaxy = max((honey[-2] - honey[0]) + (honey[i] - honey[i-1]) for i in range(1, N-1))
    print(max(rmaxy, cmaxy, lmaxy))