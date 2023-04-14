def main():
    _sum = 0
    angles = set()
    for _ in range(3):
        _sum += (angle := int(input()))
        angles.add(angle)
    if _sum != 180:
        return 'Error'
    n = len(angles)
    if n == 1:
        return 'Equilateral'
    if n == 2:
        return 'Isosceles'
    return 'Scalene'


if __name__ == '__main__':
    _type = main()
    print(_type)
