import sys
input = sys.stdin.readline


def _check(signal):
    n = len(signal)
    i = 0
    while i < n:
        if int(signal[i]):
            if signal[i:i+3] == '100':
                i += 3
            else:
                return 'NO'
            while i < n and not int(signal[i]):
                i += 1
            if not i < n:
                return 'NO'
            i += 1
            while i < n and int(signal[i]):
                i += 1
        else:
            if signal[i:i+2] == '01':
                i += 2
            elif 2 <= i and signal[i-2] == '1' and signal[i-1:i+2] == '100':
                i -= 1
            else:
                return 'NO'
    return 'YES'


class Contact():
    def __init__(self, T):
        self.answer = '\n'.join(_check(input().rstrip()) for _ in range(T))


if __name__ == '__main__':
    contacts = Contact(int(input()))
    print(contacts.answer)
