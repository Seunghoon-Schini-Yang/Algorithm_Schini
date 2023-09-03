class Rocks():
    def __init__(self, A, B, C):
        self.is_eq = 0
        if A==B==C:
            self.is_eq = 1
        elif not (A+B+C)%3:
            start = tuple(sorted([A, B, C]))
            self.visited = {start}
            queue = [start]
            self.tmp = []
            while not self.is_eq and queue:
                for A, B, C in queue:
                    if B < C:
                        self._calc(C, B, A)
                        if A < B:
                            self._calc(C, A, B)
                    else:
                        self._calc(B, A, C)
                queue = self.tmp
                self.tmp = []

    
    def _calc(self, big, small, other):
        big, small = big-small, small<<1
        if big == small == other:
            self.is_eq = 1
        else:
            seq = tuple(sorted([big, small, other]))
            if seq not in self.visited:
                self.visited.add(seq)
                self.tmp.append(seq)


if __name__ == '__main__':
    rocks = Rocks(*map(int, input().split()))
    print(rocks.is_eq)
