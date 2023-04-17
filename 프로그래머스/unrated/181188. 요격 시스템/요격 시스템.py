def solution(targets):
    targets.sort()
    cnt = 0
    cur = targets[0][1]
    for s, e in targets[1:]:
        if cur <= s:
            cnt += 1
            cur = e
        elif e < cur:
            cur = e
    return cnt + 1