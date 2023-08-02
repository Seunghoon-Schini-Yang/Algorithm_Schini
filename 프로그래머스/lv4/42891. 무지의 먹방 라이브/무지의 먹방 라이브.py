def solution(food_times, k):
    cutoff = 0
    food_times = [(time, i) for i, time in enumerate(food_times, start=1)]
    food_times.sort(key=lambda x: -x[0])
    while food_times:
        while food_times[-1][0] == cutoff:
            food_times.pop()
            if not food_times:
                return -1
        cur = food_times[-1][0]
        if len(food_times) * (cur-cutoff) <= k:
            k -= len(food_times) * (cur-cutoff)
            food_times.pop()
        else:
            k %= len(food_times)
            break
        cutoff = cur
    food_times.sort(key=lambda x: x[1])
    return food_times[k][1] if food_times else -1
