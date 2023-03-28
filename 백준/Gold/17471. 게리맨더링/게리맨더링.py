import sys
input = sys.stdin.readline
from itertools import combinations


def main():
    answer = sum(popul)

    for i in range(1, (N>>1)+1):
        for g1 in combinations(range(N), i):
            g1 = set(g1)
            g2 = set(range(N)) - g1

            g1_sum = 0
            stack = [g1.pop()]
            while stack:
                node = stack.pop()
                g1_sum += popul[node]
                for cn in graph[node]:
                    if cn in g1:
                        stack.append(cn)
                        g1.remove(cn)

            if g1: continue

            g2_sum = 0
            stack = [g2.pop()]
            while stack:
                node = stack.pop()
                g2_sum += popul[node]
                for cn in graph[node]:
                    if cn in g2:
                        stack.append(cn)
                        g2.remove(cn)            

            if g2: continue

            if abs(g1_sum - g2_sum) < answer:
                answer = abs(g1_sum - g2_sum)
    
    print(answer if answer < sum(popul) else -1)


if __name__ == '__main__':
    N = int(input())
    popul = list(map(int, input().split()))

    graph = [[] for _ in range(N)]
    for i in range(N):
        _, *adjs = map(lambda x: int(x)-1, input().split())
        graph[i] = adjs

    main()
