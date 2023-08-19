import sys
input = sys.stdin.readline


class Gifts():
    def __init__(self, N):
        extension = 0
        info = [[a, b] for a, b in zip(map(int, input().split()), map(int, input().split()))]
        for i in range(N):
            a, b = info[i]
            if a >= b:
                continue
            x = ((b-a-1)//30) + 1
            extension += x
            info[i][0] = a + 30*x

        info.sort(key=lambda x: x[1])

        thres = 0
        cur, due = info[0]
        for a, b in info:
            if b != due:
                thres = cur
                cur, due = a, b
            if a < thres:
                x = ((thres-a-1)//30) + 1
                a += 30*x
                extension += x
            cur = max(cur, a)

        self.extension = extension


if __name__ == '__main__':
    gifts = Gifts(int(input()))
    print(gifts.extension)
