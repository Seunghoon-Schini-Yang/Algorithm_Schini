import string


def main() -> str:
    mapping = {i: char for i, char in enumerate(string.ascii_uppercase, start=10)}
    mapping.update({i: str(i) for i in range(10)})
    N, B = map(int, input().split())
    
    answer = ''
    while N:
        N, r = divmod(N, B)
        answer = mapping[r] + answer
    print(answer)


if __name__ == '__main__':
    main()
