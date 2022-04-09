def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            l[i] //= 2
            i += 1
        else:
            l.pop(i)


def main():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    modify_list(l)
    print(l)


if __name__ == '__main__':
    main()