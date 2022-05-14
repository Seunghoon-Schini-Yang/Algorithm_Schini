import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol() -> None:
    while True:
        a,b = map(int, input().split())
        if not a:
            break
        
        if a > b:
            if not a % b:
                print('multiple\n')
            else:
                print('neither\n')
        else:
            if not b % a:
                print('factor\n')
            else:
                print('neither\n')


sol()
