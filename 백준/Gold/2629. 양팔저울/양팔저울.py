import sys
input = sys.stdin.readline

def solution() -> str:
    weights = map(int, input().split())
    len_b = int(input())
    beads = map(int, input().split())
    ans = ['N'] * len_b
    dp = {0}
    poss_bs = set()

    for weight in weights:
        dp_plus = set()
        for k in dp:
            poss_w = weight + k
            if poss_w not in dp:
                dp_plus.add(poss_w)
                for j in dp:
                    poss_bs.add(abs(poss_w - j))
        dp = dp.union(dp_plus)

    for i in range(len_b):
        if next(beads) in poss_bs:
            ans[i] = 'Y'
    
    return ' '.join(ans)


input()
print(solution())
