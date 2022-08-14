import sys
input = sys.stdin.readline


def calc(a: int, symbol: str, b: int) -> int:
    if symbol == '+':
        return a+b
    elif symbol == '-':
        return a-b
    else:
        return a*b


def dfs(cur_idx: int, cur_res: int) -> None:
    global maxy
    
    if cur_idx == sym_len:
        maxy = max(cur_res, maxy)
        return
    dfs(cur_idx+1, calc(cur_res, symbols[cur_idx], nums[cur_idx+1]))
    
    if cur_idx+1 == sym_len:
        return
    dfs(cur_idx+2, calc(cur_res, symbols[cur_idx], adj_cal[cur_idx+1]))
    return


if __name__ == '__main__':
    N = int(input()); sym_len = N >> 1
    equation = input().rstrip()
    nums = list(map(int, equation[::2]))
    symbols = equation[1::2]
    adj_cal = [calc(nums[i], symbols[i], nums[i+1]) for i in range(sym_len)]
    maxy = -sys.maxsize
    
    dfs(0, nums[0])
    print(maxy)
