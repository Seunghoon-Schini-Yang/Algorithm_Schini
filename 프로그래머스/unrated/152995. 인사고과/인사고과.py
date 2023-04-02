def solution(scores):
    x, y = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    memo = {}

    my = scores[0][1]
    for cx, cy in scores:
        if cy < my:
            if (cx, cy) == (x, y):
                return -1
            continue
        my = cy
        memo[cx+cy] = memo.get(cx+cy, 0) + 1
    
    goal = x + y
    acc = 0
    for score, val in sorted(memo.items(), reverse=True):
        if score == goal:
            return acc + 1
        acc += val
