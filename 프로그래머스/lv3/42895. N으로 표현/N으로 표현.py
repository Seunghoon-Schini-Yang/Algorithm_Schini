def solution(N, number):
    def calcs(x, y):
        yield x + y
        if x > y:  yield x - y
        yield x * y
        if y and x >= y:  yield x // y

    
    memo = {int(str(N) * i): i for i in range(1, 9)}
    is_break = False

    while not is_break:
        is_break = True
        tmp = {}
        for val, cnt in memo.items():
            for cval, ccnt in memo.items():
                tcnt = cnt + ccnt
                if 8 < tcnt:
                    continue
                for calc in calcs(val, cval):
                    if tcnt < memo.get(calc, 9) and tcnt < tmp.get(calc, 9):
                        is_break = False
                        tmp[calc] = tcnt
        memo.update(tmp)

    return memo.get(number, -1)
