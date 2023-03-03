import heapq
import sys
input = sys.stdin.readline


def solution(n: int) -> None:
    answer = []
    prior_q = []
    dd = {}
    for _ in range(n):
        if (num := int(input())):
            if num < 0:
                dd.update({(num := -num): dd.get(num, 0)+1})
            heapq.heappush(prior_q, num)
        else:
            if prior_q:
                if dd.get((num := heapq.heappop(prior_q)), 0):
                    answer.append(-num)
                    dd[num] -= 1
                else:
                    answer.append(num)
            else:
                answer.append(0)
    
    return '\n'.join(map(str, answer))


print(solution(int(input())))
