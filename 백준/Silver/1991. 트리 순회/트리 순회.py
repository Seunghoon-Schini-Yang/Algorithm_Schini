# my
# stack
import sys
input = sys.stdin.readline

def sol(n: int) -> str:
    btree = dict()
    for _ in range(n):
        line = input()
        btree[line[0]] = (line[4],line[2])

    stack = ['A']
    pre = []
    while stack:
        p_c = stack.pop()
        pre.append(p_c)
        if btree[p_c][0] != '.':
            stack.append(btree[p_c][0])
        if btree[p_c][1] != '.':
            stack.append(btree[p_c][1])

    stack = ['A']
    inodr = []
    visited = set()
    while stack:
        if stack[-1] in visited:
            inodr.append(stack.pop())
        else:
            visited.add(stack[-1])
            if btree[stack[-1]][0] != '.':
                stack.insert(-1, btree[stack[-1]][0])
            if btree[stack[-1]][1] != '.':
                stack.append(btree[stack[-1]][1])
            
    stack = ['A']
    post = []
    visited = set()
    while stack:
        if stack[-1] in visited:
            post.append(stack.pop())
        else:
            p_c = stack[-1]
            visited.add(p_c)
            if btree[p_c][0] != '.':
                stack.append(btree[p_c][0])
            if btree[p_c][1] != '.':
                stack.append(btree[p_c][1])
    
    return '\n'.join((''.join(pre), ''.join(inodr), ''.join(post)))


print(sol(int(input())))
