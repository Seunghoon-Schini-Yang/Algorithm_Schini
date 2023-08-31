import sys
input = sys.stdin.readline


class Pasture():
    def __init__(self, W, H):
        board = [list(input().rstrip()) for _ in range(H)]
        queue = []
        for h in range(H):
            for w in range(W):
                if board[h][w] == 'C':
                    queue.append((h, w))
        goal = queue.pop()

        dd = ((1, 0), (-1, 0), (0, 1), (0, -1))
        cnt = flag = 0
        tmp = []
        while True:
            while queue:
                ch, cw = queue.pop()
                for i in range(4):
                    dh, dw = dd[i]
                    ph, pw = ch+dh, cw+dw
                    while 0 <= ph < H and 0 <= pw < W:
                        if (ph, pw) == goal:
                            flag = True
                            self.mirrors = cnt
                            break
                        if board[ph][pw] == '.':
                            board[ph][pw] = cnt
                            tmp.append((ph, pw))
                            ph, pw = ph+dh, pw+dw
                        elif board[ph][pw] == cnt:
                            ph, pw = ph+dh, pw+dw
                        else:
                            break
                    if flag:
                        break
                if flag:
                    break
                board[ch][cw] = '*'
            if flag:
                break
            queue = tmp
            tmp = []
            cnt += 1


if __name__ == '__main__':
    pasture = Pasture(*map(int, input().split()))
    print(pasture.mirrors)
