from io import TextIOWrapper
import sys

def solution(lines: TextIOWrapper) -> None:
    p_dic = {')': '(', ']': '['}
    left = p_dic.values()

    for line in lines:
        cont = 0
        line = line.rstrip()
        if line == '.':
            break

        stack = list()
        for char in line:
            if char in left:
                stack.append(char)
            elif char in p_dic:
                if stack:
                    if p_dic[char] == stack.pop():
                        continue
                    else:
                        print('no')
                        cont = 1
                        break
                else:
                    print('no')
                    cont = 1
                    break
        
        if cont:
            continue
            
        if stack:
            print('no')
        else:
            print('yes')


solution(sys.stdin)
