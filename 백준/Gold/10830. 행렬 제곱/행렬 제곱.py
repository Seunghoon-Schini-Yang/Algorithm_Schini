import sys
input = sys.stdin.readline

def solution(n: int, exp: int) -> None:
    base_matrix = [list(map(int, input().split())) for _ in range(n)]
    return '\n'.join([' '.join(map(str, row)) for row in square(n, exp, base_matrix)])


def matrix_product(n: int, matrix_1: list, matrix_2: list) -> list:
    return [[sum(matrix_1[i][k] * matrix_2[k][j] for k in range(n)) % 1000 for j in range(n)] for i in range(n)]


def square(n: int, exp: int, base_matrix: list) -> list:
    if exp == 1:
        return [[*map(lambda x: x % 1000, row)] for row in base_matrix]
    
    matrix = square(n, exp // 2, base_matrix)
    
    if exp & 1:
        return matrix_product(n, matrix_product(n, matrix, matrix), base_matrix)
    else:
        return matrix_product(n, matrix, matrix)


print(solution(*map(int, input().split())))
