import sys
import string


def main():
    mapping = {char: i for i, char in enumerate(string.ascii_uppercase, start=10)}
    mapping.update({str(i): i for i in range(10)})
    N, B = input().split()
    B = int(B)
    
    answer, b = 0, 1
    for char in N[::-1]:
        answer += mapping[char] * b
        b *= B
    return answer


if __name__ == '__main__':
    answer = main()
    print(answer)
