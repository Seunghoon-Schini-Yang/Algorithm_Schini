def main(N: int) -> str:
    def _changes(x: int) -> str:
        tmp = []
        for unit in units:
            d, x = divmod(x, unit)
            tmp.append(d)
        return ' '.join(map(str, tmp))
    
    
    units = (25, 10, 5, 1)
    print('\n'.join(_changes(int(input())) for _ in range(N)))


if __name__ == '__main__':
    main(int(input()))
