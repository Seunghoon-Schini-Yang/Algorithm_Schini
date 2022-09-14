import sys
input = sys.stdin.readline


def is_palindrome(l: int, r: int) -> tuple:
    if l >= r:
        return 1, 1

    if word[l] != word[r]:
        return 0, 1
    
    is_true, depth = is_palindrome(l+1, r-1)
    return is_true, depth+1


if __name__ == '__main__':
    for _ in range(int(input())):
        word = input().rstrip()
        print(*is_palindrome(0, len(word)-1))
