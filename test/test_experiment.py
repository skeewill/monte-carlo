from experiment import Experiment
from pytest import approx


def test_prob_a_head():
    # heads = 1, tails = 0
    e = Experiment()
    p = e.flip_x(100_000)
    assert p == approx(0.5, rel=0.01)


# def test_prob_two_heads():
#     e = Experiment()
#     p = e.flip_twice(100_000)
#     assert p == approx(0.25, rel=0.01)


def test_prob_ththh():
    e = Experiment()
    p = e.flip_mx_n_times(5, 100_000, [0, 1, 0, 1, 1])
    assert p == approx(1 / (2**5), rel=0.05)


# Chyld's flip twice
def test_prob_hh():
    e = Experiment()
    p = e.flip_2x_n_times(100_000)
    assert p == approx(0.25, rel=0.01)
