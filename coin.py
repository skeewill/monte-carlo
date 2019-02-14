from random import randint


class Coin:
    # don't need an init since a coin doesn't have to remember anything about itself
    def flip(self):
        return randint(0, 1)

    # this not needed for Chyld's version
    def flip_twice(self):
        return [randint(0, 1), randint(0, 1)]
