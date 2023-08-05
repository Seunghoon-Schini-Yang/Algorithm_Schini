class Luna():
    def __init__(self, N, M, arr):
        if N <= M:
            self.answer = N
        else:
            s, e = 0, max(arr) * N
            while s < e:
                m = (s+e)>>1
                cur = sum(m//v for v in arr) + M
                if  cur < N:
                    s = m+1
                else:
                    e = m
            N -= sum((s-1)//v for v in arr) + M
            for i in range(M):
                if s % arr[i] == 0:
                    N -= 1
                    if N == 0:
                        self.answer = i+1
                        break

                
if __name__ == '__main__':
    cars = Luna(*map(int, input().split()), list(map(int, input().split())))
    print(cars.answer)
