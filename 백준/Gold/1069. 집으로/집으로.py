if __name__ == '__main__':
    X, Y, D, T = map(int, input().split())
    cur = pow(X**2 + Y**2, 0.5)
    ts = 0
    if D > T:
        if (2*D) < cur:
            step = ((cur - 2*D) // D) + 1
            cur -= step*D
            ts += step*T
        i = 0 if cur <= D else 1
        cur = min(
            ts + T*2,
            ts + (i+1)*T + ((i+1)*D - cur),
            ts + i*T + (cur - i*D)
        )
    print(cur)
