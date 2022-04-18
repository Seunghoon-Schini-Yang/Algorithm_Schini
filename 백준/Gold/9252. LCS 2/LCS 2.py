# dynamic programming
import sys
input = sys.stdin.readline
from collections import defaultdict

def solution(front: str, back: str) -> str:
    lcs, dp = list(), list()
    back_info = defaultdict(list)

    for i in range(len(back)-1,-1,-1):
        back_info[back[i]].append(i)

    for char in front:
        for i in back_info[char]:
            if not lcs or lcs[-1][0] < i:
                dp.append((len(lcs),char))
                lcs.append((i,char))
            else:
                lower, upper = 0, len(lcs)-1
                while lower <= upper:
                    m = (lower+upper)//2
                    if i <= lcs[m][0]:
                        upper = m-1
                    else:
                        lower = m+1
                
                if lcs[lower] == (i,char):
                    continue
                lcs[lower] = (i,char)
                dp.append((lower,char))

    ans = [0]*len(lcs)
    depth = len(lcs)-1
    for i in range(len(dp)-1,-1,-1):
        if depth < 0:
            break
        if dp[i][0]==depth:
            ans[depth] = dp[i][1]
            depth -= 1
    
    return str(len(lcs)) + '\n' + ''.join(ans)


print(solution(input().rstrip(), input().rstrip()))
