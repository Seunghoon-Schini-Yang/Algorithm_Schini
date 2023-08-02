def _search(N, arr):
    maxy = 3_000_000_000
    answer = [0, 0, 0]
    for i in range(N-2):
        s, e = i+1, N-1
        while s < e:
            cur = arr[i] + arr[s] + arr[e]
            if cur > 0:
                if cur < maxy:
                    maxy = cur
                    answer = [arr[i], arr[s], arr[e]]
                e -= 1
            elif cur < 0:
                if -cur < maxy:
                    maxy = -cur
                    answer = [arr[i], arr[s], arr[e]]
                s += 1
            else:
                return [arr[i], arr[s], arr[e]]
        if 0 <= arr[i]:
            break
    return answer


class Liquids():
    def __init__(self, N, arr):
        arr.sort()
        if 3 <= sum(True for val in arr if val == 0):
            self.answer = [0, 0, 0]
        elif 0 <= arr[0]:
            self.answer = arr[:3]
        elif arr[-1] <= 0:
            self.answer = arr[-3:]
        else:
            self.answer = _search(N, arr)


if __name__ == "__main__":
    fluids = Liquids(int(input()), list(map(int, input().split())))
    print(*fluids.answer)
