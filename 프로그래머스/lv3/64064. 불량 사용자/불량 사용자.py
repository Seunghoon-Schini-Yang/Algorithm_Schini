def solution(user_id, banned_id):
    mapping = [[] for _ in range(len(banned_id))]
    for ui, uid in enumerate(user_id):
        for bi, bid in enumerate(banned_id):
            if len(uid) != len(bid):
                continue
            for uc, bc in zip(uid, bid):
                if bc != '*' and uc != bc:
                    break
            else:
                mapping[bi].append(ui)

    cases = {0}
    for elem in mapping:
        tmp = set()
        for e in elem:
            for cas in cases:
                if cas & (1<<e):
                    continue
                tmp.add(cas ^ (1<<e))
        cases = tmp
    
    return len(cases)
