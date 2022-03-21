def solution(n: int) -> int:
    exp = max(n, 2) - 1
    matrix = [[1, 1], [1, 0]]
    result = square(exp, matrix)

    if n == 0:
        return result[1][1]
    elif n == 1 or n == 2:
        return result[0][1]
    return result[0][0]


def product(matrix_1: list, matrix_2: list) -> list:
    return [[sum(matrix_1[row][k] * matrix_2[k][col] for k in range(2)) % 1_000_000_007 for col in range(2)] for row in range(2)]


def square(exp: int, base_matrix: list) -> list:
    if exp == 1:
        return base_matrix

    matrix = square(exp // 2, base_matrix)

    if exp & 1:
        return product(product(matrix, matrix), base_matrix)
    else:
        return product(matrix, matrix)


print(solution(int(input())))
