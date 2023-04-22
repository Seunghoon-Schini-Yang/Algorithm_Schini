a, b, c, d, e, f = map(int, input().split())
det = a*e - b*d
print((e*c - b*f) // det, (a*f - d*c) // det)