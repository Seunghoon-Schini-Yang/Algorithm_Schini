import sys
input = sys.stdin.readline


class Divisor():
    def __init__(self, T):
        arr = [int(input()) for _ in range(T)]
        maxy = max(arr)+1
        acc = [i+1 for i in range(maxy+1)]
        acc[1] -= 1
        for s in range(2, (maxy>>1)+1):
            for d in range(s<<1, maxy+1, s):
                acc[d] += s
        for i in range(2, maxy+1):
            acc[i] += acc[i-1]
        self.answer = '\n'.join(map(str, [acc[v] for v in arr]))


if __name__ == '__main__':
    divisors = Divisor(int(input()))
    print(divisors.answer)
