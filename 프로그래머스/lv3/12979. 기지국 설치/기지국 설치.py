def solution(n, stations, w):
    W = 2*w + 1
    answer = cur = 0
    for station in stations:
        if cur < station-w-1:
            quot, rem = divmod(station-w-1-cur, W)
            answer += quot + (1 if rem else 0)
        cur = station+w
    
    if cur < n:
        quot, rem = divmod(n-cur, W)
        answer += quot + (1 if rem else 0)
    return answer