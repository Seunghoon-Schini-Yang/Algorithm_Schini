import sys
input = sys.stdin.readline
from collections import defaultdict

def sol(n: int) -> int:
    stack = ['1']
    graph = defaultdict(list)

    for _ in range(int(input())):
        nodes = input().split()
        graph[nodes[0]].append(nodes[1])
        graph[nodes[1]].append(nodes[0])
    visited = set()
    while stack:
        from_stack = stack.pop()
        if from_stack in visited:
            continue
        visited.add(from_stack)
        stack.extend(graph[from_stack])
    return len(visited)-1


print(sol(int(input())))
