import sys
from collections import defaultdict
input = sys.stdin.readline

def solution():
    input()

    save = defaultdict(int)
    for num in input().split():
        save[num] += 1
    
    input()
    for num in input().split():
        print(save[num], end=' ')


solution()
