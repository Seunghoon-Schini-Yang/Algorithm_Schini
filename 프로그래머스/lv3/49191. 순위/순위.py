def solution(n, results):
    adjs = [[False]*n for _ in range(n)]
    for winner, loser in results:
        adjs[winner-1][loser-1] = True
    for i in range(n):
        adjs[i][i] = True
        
    for mid in range(n):
        for i in range(n):
            if i == mid:
                continue
            for j in range(n):
                if adjs[i][j] or mid == j:
                    continue
                if adjs[i][mid] & adjs[mid][j]:
                    adjs[i][j] = True

    answer = 0
    for i in range(n):
        for j in range(n):
            if adjs[i][j] or adjs[j][i]:
                continue
            break
        else:
            answer += 1
            
    return answer

