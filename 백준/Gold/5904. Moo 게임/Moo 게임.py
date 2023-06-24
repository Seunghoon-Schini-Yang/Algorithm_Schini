if __name__ == '__main__':
    N = int(input())
    acc, t = 0, 2
    while acc + ((1<<t)-1) <= N:
        acc += (1<<t)-1
        t += 1
    while True:
        if acc < N <= acc+t+1:
            print('m' if N == acc+1 else 'o')
            break
        N -= 0 if N <= acc else acc+t+1
        t -= 1
        acc -= (1<<t)-1
