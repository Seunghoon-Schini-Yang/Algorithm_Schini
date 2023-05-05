import sys


def get_posto(preo, ino):
    if len(preo) <= 1:
        return preo
    k_i = ino.index(preo[0])
    return get_posto(preo[1:k_i+1], ino[:k_i]) + get_posto(preo[k_i+1:], ino[k_i+1:]) + preo[0]


if __name__ == '__main__':
    for query in sys.stdin.readlines():
        print(get_posto(*query.split()))
