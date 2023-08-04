from heapq import heapify, heappop

def convert(time):
    h, m = map(int, time.split(':'))
    return h*60 + m

def inverse(time):
    h, m = map(lambda x: str(x).rjust(2, '0'), divmod(time, 60))
    return h+':'+m

def solution(n, t, m, timetable):
    timetable = [convert(time) for time in timetable]
    heapify(timetable)
    last = 540+t*(n-1)
    for depart in range(540, last, t):
        for _ in range(m):
            if not timetable or depart < timetable[0]:
                break
            heappop(timetable)
    maxy = cnt = 0
    for _ in range(m):
        if not timetable or last < timetable[0]:
            break
        cnt += 1
        maxy = heappop(timetable)
    answer = last if cnt < m else maxy-1
    return inverse(answer)
