def solution(math_exp: str) -> int:
    return next(a := map(lambda x: sum(map(int, x.split('+'))), math_exp.split('-'))) - sum(a)
    

print(solution(input()))