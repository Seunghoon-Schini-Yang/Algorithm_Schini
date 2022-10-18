if __name__ == '__main__':
    N, M = int(input()), int(input())
    arr = sorted(map(int, input().split()))
    cnt, s, e = 0, 0, N-1
    while s < e:
        cursum = arr[s] + arr[e]
        if cursum < M:
            s += 1
        elif cursum > M:
            e -= 1
        else:
            cnt += 1
            s += 1; e -= 1
    print(cnt)
    