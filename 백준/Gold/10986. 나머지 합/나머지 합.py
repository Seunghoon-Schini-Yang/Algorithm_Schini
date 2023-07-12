class ResSum():
    def __init__(self):
        _, M = map(int, input().split())
        arr = list(map(int, input().split()))
        self.get_num_of_intervals(M, arr)
        
    
    def get_num_of_intervals(self, M, arr):
        memo = [0] * M
        acc = 0
        for i in arr:
            acc = (acc + i) % M
            memo[acc] += 1
        cnt = memo[0] + sum(map(lambda i: i*(i-1)//2, memo))
        self.cnt = cnt
        
    
if __name__ == '__main__':
    answer = ResSum()
    print(answer.cnt)
