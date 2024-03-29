import sys


def main():
    table = {
        'A+':   4.5,
        'A0':	4.0,
        'B+':	3.5,
        'B0':   3.0,
        'C+':	2.5,
        'C0':	2.0,
        'D+':	1.5,
        'D0':	1.0,
        'F' :	0.0
    }
    score = acc = 0.0
    for line in sys.stdin:
        _, size, grade = line.split()
        if grade == 'P':
            continue
        score += float(size) * table[grade]
        acc += float(size)
    return score / acc


if __name__ == '__main__':
    grade = main()
    print(grade)
