# dynamic programming + binary search
# bisect module 사용
import sys
input = sys.stdin.readline
from collections import defaultdict
from bisect import bisect_left


def solution(front: str, back: str) -> int:
    char_idx = defaultdict(list)
    for i in range(len(back)-1,-1,-1):
        char_idx[back[i]].append(i)

    seq = list()

    for char in front:
        for idx in char_idx[char]:
            if not seq or idx > seq[-1]:
                seq.append(idx)
            else:
                seq[bisect_left(seq,idx)] = idx
    
    return len(seq)


print(solution(input().rstrip(), input().rstrip()))
