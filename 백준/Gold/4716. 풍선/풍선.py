import sys
input = sys.stdin.readline


class Room():
    def __init__(self, balloons):
        self.balloons = balloons
    

class Teams():
    def __init__(self, arr):
        self.teams = arr
        
    
    def _sort(self):
        self.teams.sort(key=lambda x: x[1]-x[2])
        
        
    def _deliver(self, Room, idx, count):
        while self.teams:
            if Room.balloons >= self.teams[-1][0]:
                Room.balloons -= self.teams[-1][0]
                count += self.teams[-1][0] * self.teams[-1][idx]
                self.teams.pop()
            else:
                self.teams[-1][0] -= Room.balloons
                count += Room.balloons * self.teams[-1][idx]
                Room.balloons = 0
                break
        return Room, count

    
if __name__ == '__main__':
    while True:
        N, A, B = map(int, input().split())
        if N == A == B == 0:
            break
        a, b = Room(A), Room(B)
        a_team, b_team = Teams([]), Teams([])
        for _ in range(N):
            K, Da, Db = map(int, input().split())
            if Db >= Da:
                a_team.teams.append([K, Db, Da])
            else:
                b_team.teams.append([K, Da, Db])
        a_team._sort()
        b_team._sort()
        a, count = a_team._deliver(a, 2, 0)
        b, count = b_team._deliver(b, 2, count)
        if a_team.teams:
            _, count = a_team._deliver(b, 1, count)
        elif b_team.teams:
            _, count = b_team._deliver(a, 1, count)
        print(count)
