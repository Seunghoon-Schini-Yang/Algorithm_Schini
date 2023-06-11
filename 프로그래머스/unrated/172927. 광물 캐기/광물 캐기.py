def solution(picks, minerals):
    cost = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    n = min(sum(picks), ((len(minerals)-1)//5)+1)
    mapping = {"diamond": 0, "iron": 1, "stone": 2}
    minerals = [mapping[i] for i in minerals]
    minerals = [[sum(cost[k][x] for x in minerals[i:i+5]) for k in range(3)] for i in range(0, n*5, 5)]
    q = {'000': 0}
    for i in range(n):
        tmp = {}
        for mask, fat in q.items():
            mask = list(map(int, mask))
            for k in range(3):
                if mask[k] == picks[k]:
                    continue
                mask[k] += 1
                cm = ''.join(map(str, mask))
                cf = fat + minerals[i][k]
                if cm in tmp:
                    tmp[cm] = min(tmp[cm], cf)
                else:
                    tmp[cm] = cf
                mask[k] -= 1
        q = tmp       
    print(q)
    return min(q.values())
