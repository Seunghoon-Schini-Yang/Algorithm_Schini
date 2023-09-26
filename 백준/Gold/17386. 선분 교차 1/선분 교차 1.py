def make_line(x1, y1, x2, y2):
    def line(x):
        return (y2-y1) / (x2-x1) * (x-x1) + y1

    if x1 == x2:
        return 'v'
    return line


def main():
    x11, y11, x12, y12 = map(int, input().split())
    x21, y21, x22, y22 = map(int, input().split())
    (x11, y11, x12, y12) =  (x11, y11, x12, y12) if x11 <= x12 else (x12, y12, x11, y11)
    (x21, y21, x22, y22) =  (x21, y21, x22, y22) if x21 <= x22 else (x22, y22, x21, y21)
    (x11, y11, x12, y12, x21, y21, x22, y22) =\
        (x21, y21, x22, y22, x11, y11, x12, y12) if x11 == x12 else (x11, y11, x12, y12, x21, y21, x22, y22)
    line_1 = make_line(x11, y11, x12, y12)
    line_2 = make_line(x21, y21, x22, y22)

    if x11 > x22 or x12 < x21 or max(y11, y12) < min(y21, y22) or max(y21, y22) < min(y11, y12):
        print(0)
    elif (y21 - line_1(x21)) * (y22 - line_1(x22)) > 0:
        print(0)
    elif line_2 == 'v':
        print(1)
    elif (y11 - line_2(x11)) * (y12 - line_2(x12)) > 0:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    main()
