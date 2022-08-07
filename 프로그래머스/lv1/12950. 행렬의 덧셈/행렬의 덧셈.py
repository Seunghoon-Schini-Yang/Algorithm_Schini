def solution(arr1, arr2):
    return [[v1+v2 for v1, v2 in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]