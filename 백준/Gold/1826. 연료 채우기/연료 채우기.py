import sys
input = sys.stdin.readline
from heapq import heappop, heappush


class Truck():
    def __init__(self, L, P):
        self.goal = L
        self.loc = P
        self.fuels = []
        self.count = 0


if __name__ == '__main__':
    N = int(input())
    stops = [(0, 0) for _ in range(N)]
    for i in range(N):
        stops[i] = tuple(map(int, input().split()))
    stops.sort(key=lambda x: x[0])
    
    truck = Truck(*map(int, input().split()))
    i = 0
    while i < N and truck.loc < truck.goal:
        while i < N and stops[i][0] <= truck.loc:
            heappush(truck.fuels, -stops[i][1])
            i += 1
        if not truck.fuels:
            break
        truck.loc -= heappop(truck.fuels)
        truck.count += 1
    while truck.fuels and truck.loc < truck.goal:
        truck.loc -= heappop(truck.fuels)
        truck.count += 1        
    print(-1 if truck.loc < truck.goal else truck.count)
