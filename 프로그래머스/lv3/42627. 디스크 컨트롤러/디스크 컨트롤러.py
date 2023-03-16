from heapq import heappop, heappush


def solution(jobs):
    jobs.sort()
    n = len(jobs)
    i = _sum = 0

    while i < n:
        end = jobs[i][0]
        pq = [jobs[i][::-1]]
        i += 1
        
        while pq:
            cost, start = heappop(pq)
            end += cost
            _sum += end - start

            while i < n and jobs[i][0] <= end:
                heappush(pq, jobs[i][::-1])
                i += 1

    return _sum // n
