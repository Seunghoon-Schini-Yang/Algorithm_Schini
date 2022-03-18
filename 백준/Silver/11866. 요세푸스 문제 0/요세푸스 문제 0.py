class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def solution(line: str) -> None:
    print('<', end='')
    n, k = map(int, line.split())
    answer = [0] * n
    temp = node_one = Node(1)

    for i in range(2, n + 1):
        temp.next = Node(i)
        temp = temp.next
    
    temp.next = node_one

    for i in range(n):
        for _ in range(k):
            p = temp
            temp = temp.next
        answer[i] = str(temp.val)
        p.next = temp.next
        temp = p

    print(', '.join(answer), end='')
    print('>')


solution(input())
