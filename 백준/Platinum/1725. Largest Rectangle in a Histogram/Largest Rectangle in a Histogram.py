import sys
input = sys.stdin.readline


def main(N):
    stack = [[0, 0]]
    arr = [int(input()) for _ in range(N)]
    arr.append(0)
    area = 0

    for h in arr:
        acc = 0
        while h < stack[-1][0]:
            ch, ccc = stack.pop()
            acc += ccc
            area = max(area, ch * acc)
        acc += 1

        if stack[-1][0] == h:
            stack[-1][1] += acc
        else:
            stack.append([h, acc])

    return area


if __name__ == '__main__':
    largest_area = main(int(input()))
    print(largest_area)
