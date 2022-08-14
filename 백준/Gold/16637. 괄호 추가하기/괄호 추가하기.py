import sys
input = sys.stdin.readline


def calc(a: int, symbol: str, b: int) -> int:
    if symbol == '+':
        return a+b
    elif symbol == '-':
        return a-b
    else:
        return a*b


def minmax(a: int, b: int) -> tuple:
    return (a,b) if b > a else (b,a)


def dfs(cur_idx: int) -> None:
    if cur_idx == sym_len:
        return
    n_min, n_max = minmax(calc(memo_max[cur_idx], symbols[cur_idx], nums[cur_idx+1]), calc(memo_min[cur_idx], symbols[cur_idx], nums[cur_idx+1]))
    is_dfs = False
    if memo_max[cur_idx+1] < n_max:
        memo_max[cur_idx+1] = n_max
        is_dfs = True
    if memo_min[cur_idx+1] > n_min:
        memo_min[cur_idx+1] = n_min
        is_dfs = True
    if is_dfs:
        dfs(cur_idx+1)
    
    if cur_idx+1 == sym_len:
        return
    n_min, n_max = minmax(calc(memo_max[cur_idx], symbols[cur_idx], adj_cal[cur_idx+1]), calc(memo_min[cur_idx], symbols[cur_idx], adj_cal[cur_idx+1]))
    is_dfs = False
    if memo_max[cur_idx+2] < n_max:
        memo_max[cur_idx+2] = n_max
        is_dfs = True
    if memo_min[cur_idx+2] > n_min:
        memo_min[cur_idx+2] = n_min
        is_dfs = True
    if is_dfs:
        dfs(cur_idx+2)
    return


if __name__ == '__main__':
    INF = sys.maxsize
    sym_len = int(input()) >> 1
    equation = input().rstrip()
    nums = list(map(int, equation[::2]))
    symbols = equation[1::2]
    adj_cal = [calc(nums[i], symbols[i], nums[i+1]) for i in range(sym_len)]
    memo_max = [-INF]*(sym_len+1)
    memo_min = [INF]*(sym_len+1)
    memo_max[0] = memo_min[0] = nums[0]
    
    dfs(0)
    print(memo_max[-1])
