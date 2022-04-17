import sys
input = sys.stdin.readline


def solution(array: list) -> int:
    set_array = set(array)
    idx_info = dict((num, i) for i, num in enumerate(sorted(set_array)))
    order_list = [0] * len(set_array)

    for num in array:
        idx = idx_info[num]
        if idx:
            order_list[idx] =  max(order_list[:idx]) + 1
        else:
            order_list[idx] = 1
        
    return max(order_list)


input()
print(solution(list(map(int, input().split()))))
