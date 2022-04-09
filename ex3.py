import random

class Cat():
    def __init__(self, kittens):
        self.male = random.randrange(0, kittens)
        self.female = kittens - self.male

    def male(self):
        return self.male

    def female(self):
        return self.female


def main():
    cat1 = Cat(8)
    print(cat1.male, cat1.female)


if __name__ == '__main__':
    main()