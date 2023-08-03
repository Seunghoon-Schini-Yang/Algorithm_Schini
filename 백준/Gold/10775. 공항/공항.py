import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 9))


class Airport():
    def __init__(self, G, P):
        self.warp = [i for i in range(G+1)]
        for i in range(1, P+1):
            g = int(input())
            self.warp[g] = self._find(g)
            if self.warp[g] == -1:
                i -= 1
                break
        self.answer = i
        
    
    def _find(self, gate):
        if self.warp[gate] == gate:
            self.warp[gate] = gate-1
        else:
            self.warp[gate] = self._find(self.warp[gate])
        return self.warp[gate]
    

if __name__ == '__main__':
    port = Airport(int(input()), int(input()))
    print(port.answer)
