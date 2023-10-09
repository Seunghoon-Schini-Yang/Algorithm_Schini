class Buildings():
    def __init__(self, n):
        self.n = n
        self.heights = list(map(int, input().split()))


def main():
    bs = Buildings(int(input()))
    if bs.n == 1:
        print(0)
    else:
        sights = [2] * bs.n
        sights[0] = sights[-1] = 1
        for i in range(bs.n - 2):
            slope = bs.heights[i+1] - bs.heights[i]
            for j in range(i+2, bs.n):
                cur = (bs.heights[j] - bs.heights[i]) / (j - i)
                if cur <= slope:
                    continue
                sights[i] += 1
                sights[j] += 1
                slope = cur
        print(max(sights))


if __name__ == '__main__':
    main()
