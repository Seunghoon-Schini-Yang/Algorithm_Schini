def rec(x):
    if x <= 1:
        return 1
    return x * rec(x-1)


if __name__ == '__main__':
    print(rec(int(input())))
