def solution(k, tangerine):
    counts = {}
    for tang in tangerine:
        counts[tang] = counts.get(tang, 0) + 1
    cur = 0
    for i, cnt in enumerate(sorted(counts.values(), reverse=True)):
        cur += cnt
        if cur >= k:
            break
    return i+1
