import sys
input = sys.stdin.readline

C = int(input())
for _ in range(C):
    class_info = list(map(int, input().split()))
    student_num = class_info[0]
    grades = class_info[1:]
    grades_sum = sum(grades)
    booleans = [True if grade > grades_sum / student_num else False for grade in grades]
    print(f'{sum(booleans) / student_num * 100:.3f}%')