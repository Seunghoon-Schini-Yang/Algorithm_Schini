def solution(expression):
    def _count(seq, nums, syms, sym_loc):
        for si in seq:
            cur = sym_loc[si]
            i = 0
            while i < len(syms):
                if syms[i] == cur:
                    if cur == '+':
                        nums[i] += nums[i+1]
                    elif cur == '-':
                        nums[i] -= nums[i+1]
                    else:
                        nums[i] *= nums[i+1]
                    del nums[i+1], syms[i]
                else:
                    i += 1
        return abs(nums[0])
    

    si = 0
    nums = []
    syms = []
    for i, char in enumerate(expression):
        if char in ('+', '-', '*'):
            nums.append(int(expression[si:i]))
            syms.append(char)
            si = i+1
    nums.append(int(expression[si:]))

    sym_cnt = {}
    for sym in syms:
        sym_cnt[sym] = sym_cnt.get(sym, 0) + 1
    sym_loc = list(sym_cnt.keys())

    if len(sym_cnt) == 1:
        return _count((0,), nums[:], syms[:], sym_loc)
    elif len(sym_cnt) == 2:
        return max(_count(seq, nums[:], syms[:], sym_loc) for seq in ((0, 1), (1, 0)))
    else:
        return max(_count(seq, nums[:], syms[:], sym_loc) for seq in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0)))
