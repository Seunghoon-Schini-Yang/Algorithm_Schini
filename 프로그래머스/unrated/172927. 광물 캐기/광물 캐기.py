def bfs():
    return


def solution(picks, minerals):
    mapping = {"diamond": 0, "iron": 1, "stone": 2}
    minerals = [mapping[i] for i in minerals]
    cost = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    q = {0: [picks, 0]}
    for i in range(0, min(sum(picks)*5, len(minerals)), 5):
        tmp = {}
        for mask, (res, fat) in q.items():
            for k in range(3):
                if not res[k]:
                    continue
                cres = res.copy()
                cres[k] -= 1
                cm = mask + 6**k
                cf = fat + sum(cost[k][minerals[x]] for x in range(i, min(i+5, len(minerals))))
                if cm in tmp:
                    tmp[cm][1] = min(tmp[cm][1], cf)
                else:
                    tmp[cm] = [cres, cf]
        q = tmp       

    return min(x for _, x in q.values())