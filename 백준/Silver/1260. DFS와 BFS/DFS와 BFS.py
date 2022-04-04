import sys
input = sys.stdin.readline
from collections import defaultdict, deque

def sol(n: int, e: int, s: int) -> str:
    graph = defaultdict(set)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)
    
    for k, v in graph.items():
        graph[k] = sorted(v, reverse=True)

    stack, queue = deque([s]), deque([s])
    ans = [[], []]

    check = set()
    while stack:
        from_stack = stack.pop()
        if from_stack in check:
            continue
        check.add(from_stack)
        ans[0].append(str(from_stack))
        stack.extend(graph[from_stack])

    check = set()
    while queue:
        temp = list()
        for _ in range(len(queue)):
            from_queue = queue.pop()
            if from_queue in check:
                continue
            check.add(from_queue)
            ans[1].append(str(from_queue))
            temp.append(graph[from_queue])
        while temp:
            queue.extend(temp.pop())
        

    return '\n'.join(' '.join(search) for search in ans)


print(sol(*map(int, input().split())))
