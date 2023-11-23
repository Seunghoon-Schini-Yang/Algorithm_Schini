def solution(s):
    def get_converted(x):
        converted = []
        ones_conseq = target = 0
        
        for bit in map(int, x):
            if bit:
                ones_conseq += 1
            else:
                if ones_conseq <= 1:
                    converted += [1] * ones_conseq + [0]
                    ones_conseq = 0
                else:
                    target += 1
                    ones_conseq -= 2
        
        converted += [1, 1, 0] * target + [1] * ones_conseq
        return ''.join(map(str, converted))
    
    return [get_converted(x) for x in s]
