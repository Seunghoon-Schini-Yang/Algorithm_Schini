import sys
from collections import defaultdict
input = sys.stdin.readline


def solution(front: str, back: str) -> int:
    char_idx = defaultdict(list)
    for i in range(len(back) - 1, -1, -1):
        char_idx[back[i]].append(i)
        
    seq = list()

    for char in front:
        for idx in char_idx[char]:
            if not seq or idx > seq[-1]:
                seq.append(idx)
            else:
                seq[binary_search(0, len(seq) - 1, idx, seq)] = idx
    
    return len(seq)


def binary_search(l: int, r: int, idx: int, seq: list) -> int:
    while l <= r:
        m = (l + r) // 2

        if idx <= seq[m]:
            r = m - 1
        else:
            l = m + 1
    return l


print(solution(input().rstrip(), input().rstrip()))
