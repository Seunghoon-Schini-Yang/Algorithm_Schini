import sys
input = sys.stdin.readline


if __name__ == '__main__':
    pos = []; neg = []; ones = 0
    for _ in range(int(input())):
        if (x := int(input())) <= 0:  neg.append(x)
        elif x == 1:  ones += 1
        else:  pos.append(x)
    pos.sort()
    neg.sort(reverse=True)
    pl, nl = len(pos), len(neg)
    acc = 0
    while 2 <= nl:
        acc += neg.pop() * neg.pop()
        nl -= 2
    while 2 <= pl:
        acc += pos.pop() * pos.pop()
        pl -= 2
    print(acc + (neg[0] if nl else 0) + (pos[0] if pl else 0) + ones)
