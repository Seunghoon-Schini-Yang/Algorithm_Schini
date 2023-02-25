import sys
input = sys.stdin.readline


def main():
    S, T = input().rstrip(), input().rstrip()
    s_len = len(S)
    is_visited = set()

    stack = [T]
    while stack:
        string = stack.pop()
        if len(string) == s_len:
            if string == S:
                return 1
            continue

        if string[0] == 'B' and string[1:][::-1] not in is_visited:
            stack.append(string[1:][::-1])
            is_visited.add(string[1:][::-1])
        if string[-1] == 'A' and string[:-1] not in is_visited:
            stack.append(string[:-1])
            is_visited.add(string[:-1])
    return 0


if __name__ == '__main__':
    print(main())
