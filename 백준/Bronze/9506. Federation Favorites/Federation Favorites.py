import sys
input = sys.stdin.readline


def main():
    while (n := int(input())) != -1:
        a = []; b = []
        for i in range(1, int(pow(n ,0.5))+1):
            if not n % i:
                a.append(i)
                b.append(n // i)
        if a[-1] == b[-1]:
            b.pop()
        a += b[::-1]
        a.pop()
        if n == sum(a):
            print(f'{n} = ' + ' + '.join(map(str, a)))
        else:
            print(f'{n} is NOT perfect.')


if __name__ == '__main__':
    main()
