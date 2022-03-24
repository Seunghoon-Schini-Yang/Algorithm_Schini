def solution():
    n, k = int(input()), int(input())
    start, end = 1, n*n
    while start <= end:
        mid = (start + end) // 2
        base = mid//n
        cnt = base * n
        for i in range(base+1, min(n, mid)+1):
            cnt += mid//i
        
        if cnt >= k:
            end = mid - 1
        else:
            start = mid + 1

    return start


print(solution())
