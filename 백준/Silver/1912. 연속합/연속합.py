import sys
input = sys.stdin.readline

def solution(seq_map: map) -> int:
    maxi = next(seq_map)
    seq_part_sum = max(maxi, 0)
    
    for num in seq_map:
        c_sum = seq_part_sum + num
        if c_sum <= 0:
            seq_part_sum = 0
            maxi = max(maxi, num)
            continue
        seq_part_sum = c_sum
        maxi = max(maxi, seq_part_sum)

    return maxi


input()
print(solution(map(int, input().split())))