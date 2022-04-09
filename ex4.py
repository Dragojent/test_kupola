def wrap_num(value, min_value, max_value):
    return min_value if value > max_value else value

def calc_neighbors(p_numbers):
    if len(p_numbers) == 1:
        return p_numbers

    neighbors = []
    numbers = list(map(int, p_numbers.split()))
    for i in range(len(numbers)):
        neighbors.append(numbers[wrap_num(i + 1, 0, len(numbers) - 1)] + numbers[i - 1])

    return ' '.join([str(i) for i in neighbors])


def main():
    numbers = "1 2 3 4 5 6 7 8 9 10"
    print(calc_neighbors(numbers))


if __name__ == '__main__':
    main()