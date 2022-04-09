def make_dict(a, b):
    dic = {}
    for i in range(len(a)):
        dic[a[i]] = b[i] if i < len(b) else None

    return dic

def main():
    a, b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ["a", "b", "c"]
    dic = make_dict(a, b)
    print(dic)


if __name__ == '__main__':
    main()