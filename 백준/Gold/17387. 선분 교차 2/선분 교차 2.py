class Lines():
    def __init__(self):
        err = 1e-8
        l1x1, l1y1, l1x2, l1y2 = map(int, input().split())
        l2x1, l2y1, l2x2, l2y2 = map(int, input().split())
        slope1 = 'v' if l1x1 == l1x2 else (l1y2-l1y1) / (l1x2-l1x1)
        slope2 = 'v' if l2x1 == l2x2 else (l2y2-l2y1) / (l2x2-l2x1)
        if slope1 == 'v':
            if l1y2 < l1y1:
                l1y1, l1y2 = l1y2, l1y1
            if slope2 == 'v':
                if l2y2 < l2y1:
                    l2y1, l2y2 = l2y2, l2y1
                if l1x1 != l2x1:
                    self.answer = 0
                else:
                    if l2y2 < l1y1 or l1y2 < l2y1:
                        self.answer = 0
                    elif l1y1 == l2y2:
                        self.answer = 1
                    elif l2y1 == l1y2:
                        self.answer = 1
                    else:
                        self.answer = 1
            else:
                y = slope2*(l1x1 - l2x1) + l2y1
                if l2x2 < l2x1:
                    l2x1, l2x2 = l2x2, l2x1
                if l1y1-err <= y <= l1y2+err and l2x1 <= l1x1 <= l2x2:
                    self.answer = 1
                else:
                    self.answer = 0
        elif slope2 == 'v':
            if l2y2 < l2y1:
                l2y1, l2y2 = l2y2, l2y1
            y = slope1*(l2x1 - l1x1) + l1y1
            if l1x2 < l1x1:
                l1x1, l1x2 = l1x2, l1x1
            if l2y1-err <= y <= l2y2+err and l1x1 <= l2x1 <= l1x2:
                self.answer = 1
            else:
                self.answer = 0
        elif abs(slope1 - slope2) < err:
            thres = slope1 * (l1x1 - l2x1)
            if thres-err < l1y1 - l2y1 < thres+err :
                if l1x2 < l1x1:
                    l1x1, l1y1, l1x2, l1y2 = l1x2, l1y2, l1x1, l1y1
                if l2x2 < l2x1:
                    l2x1, l2y1, l2x2, l2y2 = l2x2, l2y2, l2x1, l2y1
                if l2x2 < l1x1 or l1x2 < l2x1:
                    self.answer = 0
                elif l2x2 == l1x1:
                    self.answer = 1
                elif l1x2 == l2x1:
                    self.answer = 1
                else:
                    self.answer = 1
            else:
                self.answer = 0
        else:
            x = (l2y1 - l1y1 + slope1*l1x1 - slope2*l2x1) / (slope1 - slope2)
            if l1x2 < l1x1:
                l1x1, l1x2 = l1x2, l1x1
            if l2x2 < l2x1:
                l2x1, l2x2 = l2x2, l2x1
            if l1x1-err <= x <= l1x2+err and l2x1-err <= x <= l2x2+err:
                self.answer = 1
            else:
                self.answer = 0
        

if __name__ == '__main__':
    lines = Lines()
    print(lines.answer)
