def multiply(a: int, b: int) -> int:
    return a*b


if __name__ == '__main__':
    tot = int(input())
    print('Yes' if sum(multiply(*map(int, input().split())) for _ in range(int(input()))) == tot else 'No')
