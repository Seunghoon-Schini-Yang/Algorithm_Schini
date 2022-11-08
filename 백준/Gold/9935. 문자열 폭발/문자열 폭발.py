import sys
input = sys.stdin.readline


if __name__ == '__main__':
    string = input().strip(); s_len = len(string); si= 0
    key = input().strip(); k_len = len(key); ki = 0
    stack = list()
    result = ''

    while si < s_len:
        if ki == k_len:
            ki = stack.pop() if stack else 0
        elif string[si] == key[ki]:
            si += 1; ki += 1
        # string[si] != key[ki]
        elif not ki:
            for i in stack:
                result += key[:i]
            stack = list()
            result += string[si]
            si += 1
        else:
            stack.append(ki)
            ki = 0

    for i in stack:
        result += key[:i]
    if ki != k_len:
        result += key[:ki]

    print(result if result else 'FRULA')
