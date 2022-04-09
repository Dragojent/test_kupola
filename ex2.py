def extract_numbers(string):
    return [int(i) for i in string.split() if (i[0].isdigit())]

def main():
    a = "asd 12 sdf 34 gf 567 fd 8 9"
    print(extract_numbers(a))


if __name__ == '__main__':
    main()