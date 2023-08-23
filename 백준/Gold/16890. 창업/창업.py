class CompanyName():
    def __init__(self, koo, cube):
        N = len(koo)
        koo = sorted(koo, reverse=True)[~((N>>1)+(1 if N&1 else 0))+1:]
        cube = sorted(cube)[~(N>>1)+1:] if N>1 else []
        head, tail = [], []
        turn = 0
        while koo and cube and koo[-1] < cube[-1]:
            if turn:
                head.append(cube.pop())
            else:
                head.append(koo.pop())
            turn ^= 1
        koo = koo[::-1]
        cube = cube[::-1]
        while koo and cube:
            if turn:
                tail.append(cube.pop())
            else:
                tail.append(koo.pop())
            turn ^= 1
        self.final = head + (koo if koo else cube) + tail[::-1]


if __name__ == '__main__':
    cands = CompanyName(input().rstrip(), input().rstrip())
    print(''.join(cands.final))
