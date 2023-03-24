from collections import deque


def main():
    N, K = map(int, input().split())
    N2 = N<<1
    belt = list(map(int, input().split()))
    on, off = 0, N-1
    is_robot = [False] * N2
    step = zeros = 0

    while zeros < K:
        step += 1
        # 1
        on = (on-1) % N2
        off = (off-1) % N2
        is_robot[off] = False
        # 2
        for i in range(on+N-2, on-1, -1):
            if not is_robot[i%N2]:
                continue
            if is_robot[(i+1)%N2] or not belt[(i+1)%N2]:
                continue
            is_robot[i%N2] = False
            is_robot[(i+1)%N2] = True
            belt[(i+1)%N2] -= 1
            if not belt[(i+1)%N2]:
                zeros += 1
        is_robot[off] = False
        # 3
        if belt[on]:
            is_robot[on] = True
            belt[on] -= 1
            if not belt[on]:
                zeros += 1

    print(step)


if __name__ == '__main__':
    main()
