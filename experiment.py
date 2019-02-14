from coin import Coin


class Experiment:
    def flip_x(self, x):
        # return the probabiliy of flipping a head
        c = Coin()
        return sum((c.flip() for _ in range(x))) / x

    def flip_twice(self, x):
        # return the probability of flipping two heads
        c = Coin()
        lst = [c.flip_twice() for _ in range(x)]
        num = lst.count([1, 1])
        return num / x

    # Chyld's flip twice
    def flip_2x_n_times(self, n):
        # n is how many times you're running the experiment
        c = Coin()
        experiments = [sum([c.flip(), c.flip()]) == 2 for _ in range(n)]
        return sum(experiments) / n

    def flip_mx_n_times(self, m, n, des):
        # m is the number of flips
        # n i s the number of experiments
        c = Coin()
        experiments = []
        for _ in range(n):
            order = []
            for _ in range(m):
                order.append(c.flip())
            if order == des:
                experiments.append(order)
        return len(experiments) / n
        # this can be written using a single list comprehension

    # Chyld's pattern flip
    def flip_coin_with_pattern_n_times(self, pattern, n, flips):
        c = Coin()
        experiments = [[c.flip() for f in range(flips)] == pattern for e in range(n)]
        return sum(experiments) / n
