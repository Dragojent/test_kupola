def calc_readable(n):
    value = []
    k = n
    for i in range(n):
        for j in range(i + 1):
            value.append(str(i + 1))
            k = k - 1
            if k <= 0:
                return ' '.join(value)


def calc_comprehension(n):  #incomprehensible
    return ' '.join(str(k[0]) for k in zip([i + 1 for i in range(n) for j in range(i + 1)], range(n)))


def main():
    print(calc_readable(8))
    print(calc_comprehension(8))


if __name__ == '__main__':
    main()