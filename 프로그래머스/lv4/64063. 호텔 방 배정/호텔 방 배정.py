import sys
sys.setrecursionlimit(pow(10, 9))


class Hotel():
    def __init__(self, k, query):
        self.memo = {}
        for i in range(len(query)):
            self.memo[query[i]] = self._find(query[i])
            query[i] = self.memo[query[i]] - 1
        self.query = query
        
    def _find(self, q):
        p = self.memo.get(q, -1)
        if p == -1:
            return q+1
        self.memo[p] = self._find(p)
        return self.memo[p]

    
def solution(k, room_number):
    hotel = Hotel(k, room_number)
    return hotel.query