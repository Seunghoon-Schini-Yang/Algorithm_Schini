import sys
from collections import Counter
input = sys.stdin.readline

def solution():
    input()
    counter = Counter(input().split())
    input()
    print(' '.join(str(counter[num]) if num in counter else '0' for num in input().split()))


solution()
