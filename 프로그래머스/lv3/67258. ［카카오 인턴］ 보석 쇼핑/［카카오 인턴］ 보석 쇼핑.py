from collections import deque


def solution(gems):
    counter = {gem: 0 for gem in set(gems)}
    n = len(gems)
    n_gem = len(counter)
    init_gems = set()
    i = j = 0
    dq = deque()
    
    # init
    while j < n and len(init_gems) < n_gem:
        init_gems.add(gems[j])
        dq.append(gems[j])
        counter[gems[j]] += 1
        while 1 < counter[dq[0]]:
            counter[dq.popleft()] -= 1
            i += 1
        j += 1

    n_shop = j - i
    if n_shop == n_gem:
        return [i+1, j]
    xi = i+1; xj = j

    for gem in gems[j:]:
        counter[gem] += 1
        dq.append(gem)
        while 1 < counter[dq[0]]:
            counter[dq.popleft()] -= 1
            i += 1
        j += 1
        if j - i < n_shop:
            n_shop = j - i
            xi = i+1; xj = j

    return [xi, xj]
