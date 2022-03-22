import sys
input = sys.stdin.readline
import math

class SegmentTree:
    def __init__(self, arr: list) -> None:
        self.arr = arr

        seg_list = [0] * (seg_len := pow(2, math.ceil(math.log2((n := len(arr)))) + 1))
        self.seg_list = seg_list
        self.init_seg(0, n)


    def init_seg(self, s_idx: int, e_idx: int ,idx: int=1):
        if s_idx + 1 == e_idx:
            self.seg_list[idx] = [(s_idx, e_idx), self.arr[s_idx]]
            return self.arr[s_idx]
        else:
            mid = (s_idx + e_idx) // 2
            val = self.init_seg(s_idx, mid, idx * 2) + self.init_seg(mid, e_idx, idx * 2 + 1)
            self.seg_list[idx] = [(s_idx, e_idx), val]
            return val


    def get_sum(self, s_idx: int, e_idx: int, idx: int=1) -> int:
        if s_idx == (seg_idx := self.seg_list[idx])[0][0] and e_idx == seg_idx[0][1]:
            return seg_idx[1]
        if s_idx >= (mid := (seg_idx[0][0] + seg_idx[0][1]) // 2):
            return self.get_sum(s_idx, e_idx, idx * 2 + 1)
        if e_idx <= mid:
            return self.get_sum(s_idx, e_idx, idx * 2)
        return self.get_sum(s_idx, mid, idx * 2) + self.get_sum(mid, e_idx, idx * 2 + 1)


    def update(self, idx: int, val: int, seg_i: int=1) -> None:
        if idx == (seg_idx := self.seg_list[seg_i])[0][0] and idx + 1 == seg_idx[0][1]:
            self.arr[idx] = val
            diff = val - seg_idx[1]
            seg_idx[1] = val
        elif idx >= (mid := (seg_idx[0][0] + seg_idx[0][1]) // 2):
            seg_idx[1] += (diff := self.update(idx, val, seg_i * 2 + 1))
        else:
            seg_idx[1] += (diff := self.update(idx, val, seg_i * 2))
        return diff


def solution(n: int, m: int, k: int) -> None:
    seg_tree = SegmentTree([int(input()) for _ in range(n)])

    for _ in range(m + k):
        a, b, c = input().split()
        if a == '1':
            seg_tree.update(int(b) - 1, int(c))
        else:
            print(seg_tree.get_sum(int(b) - 1, int(c)))


solution(*map(int, input().split()))
