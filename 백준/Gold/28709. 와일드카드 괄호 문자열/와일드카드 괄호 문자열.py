import sys
input = sys.stdin.readline


class Strings():
    def __init__(self, T):
        self.is_correct = [self._is_correct(input().rstrip()) for _ in range(T)]


    def _is_correct(self, word):
        is_wc = False
        shorten = []
        for char in word:
            if char == '(':
                shorten.append('(')
            elif char == ')':
                if shorten and shorten[-1] == '(':
                    shorten.pop()
                else:
                    shorten.append(')')
            elif char == '?':
                shorten.append(')' if is_wc else '?')
            else:
                if not is_wc:
                    is_wc = True
                    l = r = 0
                    for char in shorten:
                        if char == '(' or char == '?':
                            l += 1
                        else:
                            r += 1
                        if l < r:
                            return 'NO'
                shorten = []
        
        if shorten and ((not is_wc and shorten[0] == ')') or shorten[-1] == '('):
            return 'NO'

        if is_wc:
            l = r = 0
            for char in shorten[::-1]:
                if char == ')':
                    r += 1
                else:
                    l += 1
                if r < l:
                    return 'NO'
            return 'YES'
        else:
            if len(shorten)&1:
                return 'NO'
            
            l = r = q = 0
            for char in shorten:
                if char == '(':
                    l += 1
                elif char == '?':
                    q += 1
                else:
                    r += 1
                if l+q < r:
                    return 'NO'
            if l+q < r or r+q < l:
                return 'NO'
            
            l = r = q = 0
            for char in shorten[::-1]:
                if char == '(':
                    l += 1
                elif char == '?':
                    q += 1
                else:
                    r += 1
                if r+q < l:
                    return 'NO'
            return 'YES'


if __name__ == '__main__':
    strings = Strings(int(input()))
    print('\n'.join(map(str, strings.is_correct)))
