def solution(target):
    memo = [[0, 0] for _ in range(max(70, target)+1)]
    for i in range(1, 21):
        memo[i] = [1, 1]
    for i in range(21, 41):
        memo[i] = [1, 0]
    for i in (23, 25, 29, 31, 35, 37):
        memo[i] = [2, 2]
    for i in range(41, 50):
        memo[i] = [2, 1]
    memo[50] = [1, 1]
    for i in range(52, 71):
        memo[i] = [2, 2]
    for i in range(42, 61, 3):
        memo[i] = [1, 0]
    
    for i in range(71, target+1):
        sty = i-60
        fty = i-50
        tf = False
        if memo[sty][0] < memo[fty][0]:
            tf = True
        elif memo[sty][0] == memo[fty][0]:
            if memo[fty][1] < memo[sty][1]:
                tf = True
        if tf:
            memo[i] = [memo[sty][0]+1, memo[sty][1]]
        else:
            memo[i] = [memo[fty][0]+1, memo[fty][1]+1]
    
    return memo[target]