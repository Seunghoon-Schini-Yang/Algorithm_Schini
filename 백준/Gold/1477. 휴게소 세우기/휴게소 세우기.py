def main():
    N, M, L = map(int, input().split())
    rests = list(map(int, input().split()))
    rests.sort()
    rests = [0] + rests + [L]
    rests = [rests[i+1] - rests[i] - 1 for i in range(N+1)]
    
    s, e = 1, L
    while s < e:
        mid = (s+e)>>1
        cnt = sum(step // mid for step in rests)
        if cnt <= M:
            e = mid
        else:
            s = mid + 1
    print(s)


if __name__ == '__main__':
    main()
