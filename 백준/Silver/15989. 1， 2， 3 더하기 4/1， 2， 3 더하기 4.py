import sys
input = sys.stdin.readline


def count_cases(n):
    if n <= 3:
        return n
    answer = 0
    if n % 6 < 3:
        answer += (n>>1) + 1
        answer += count_cases(n-3)
    else:
        answer += (n//3) + 1
        answer += ((n>>1)+((n%3)>>1)) * (((n//3)+1)>>1)
    return answer


if __name__ == '__main__':
    for _ in range(int(input())):
        print(count_cases(int(input())))
