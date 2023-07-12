class ResSum():
    def __init__(self):
        self.N, self.M = map(int, input().split())
        self.arr = list(map(int, input().split()))
        self.get_num_of_intervals()
        
    
    def get_num_of_intervals(self):
        memo = [0] * self.M
        acc = 0
        for i in self.arr:
            acc = (acc + i) % self.M
            memo[acc] += 1
        cnt = memo[0] + sum(map(lambda i: i*(i-1)//2, memo))
        self.cnt = cnt
        
    
if __name__ == '__main__':
    answer = ResSum()
    print(answer.cnt)
