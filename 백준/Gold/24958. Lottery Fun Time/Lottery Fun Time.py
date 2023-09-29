import sys
input = sys.stdin.readline


class Lottery():
    def __init__(self, N):
        numbers = [[0] * 100 for _ in range(100)]
        for _ in range(N):
            number = input().rstrip()
            numbers[int(number[4:6])][int(number[2:4])] += 1
        cands = []
        for i in range(100):
            _sum = _max = 0
            for j in range(100):
                _sum += numbers[i][j]
                _max = numbers[i][j] if _max < numbers[i][j] else _max
            if _sum:
                cands.append((_sum, _max*8))
        cands.sort(key=lambda x: x[1], reverse=True)
        self.second = [s for _, s in cands]
        self.third = [(t, i) for i, (t, _) in enumerate(cands)]
        self.third.sort(key=lambda x: x[0], reverse=True)


def main():
    tickets = Lottery(int(input()))
    second, third = tickets.second, tickets.third
    n = len(third)

    if n >= 5:
        prize = 0
        for i in range(3):
            if third[i][1] >= 3:
                continue
            else:
                idx = third[i][1]
                cur = second[idx]
                for j in range(4):
                    if j == idx:
                        continue
                    cur += third[j][0]
                prize = max(prize, cur)
        
        idxs = [third[i][1] for i in range(3)]
        i = 0
        while i in idxs:
            i += 1
        prize = max(prize, sum(third[idx][0] for idx in range(3)) + second[i]) + 600

    elif n > 1:
        if n == 4:
            prize = sum(third[i][0] for i in range(3)) + 600
        else:
            prize = sum(third[i][0] for i in range(n-1)) + max(third[n-1][0], 600)
        
        for i in range(n):
            cur = second[i]
            *idxs, li = [idx for idx in range(n) if idx != i]
            for idx in idxs:
                cur += third[idx][0]
            cur += max(third[li][0], 600)
            prize = max(prize, cur)
        
    else:
        prize = max(third[0][0], second[0], 600)
        
    print(prize * 500)


if __name__ == '__main__':
    main()
