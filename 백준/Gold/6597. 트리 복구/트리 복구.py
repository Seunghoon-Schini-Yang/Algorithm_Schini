import sys


def recur(preo, ino):
    if len(preo) <= 1:
        return preo
    _key = preo[0]
    k_i = ino.index(_key)
    return recur(preo[1:k_i+1], ino[:k_i]) + recur(preo[k_i+1:], ino[k_i+1:]) + _key


if __name__ == '__main__':
    for query in sys.stdin.readlines():
        print(recur(*query.split()))
        