def gcd(x, y):
    if x%y:
        return gcd(y, x%y)
    return y


if __name__ == '__main__':
    s1, m1 = map(int, input().split())
    s2, m2 = map(int, input().split())
    s = s1*m2 + s2*m1
    m = m1 * m2
    sm = gcd(m, s)
    print(s//sm, m//sm)