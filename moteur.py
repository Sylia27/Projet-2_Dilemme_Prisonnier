import random
from itertools import combinations

PAYOFF = {("C", "C"): (3, 3), ("C", "D"): (0, 5),
          ("D", "C"): (5, 0), ("D", "D"): (2, 2)}


def play_match(s1, s2, rng, rounds=200):
    h1, h2 = [], []
    sc1 = sc2 = 0
    for _ in range(rounds):
        m1 = s1.play(h1, h2, rng)
        m2 = s2.play(h2, h1, rng)
        g1, g2 = PAYOFF[(m1, m2)]
        sc1 += g1
        sc2 += g2
        h1.append(m1)
        h2.append(m2)
    return sc1, sc2


def tournament(strategies, rng, games=5, rounds=200):
    totals = {s.name: 0 for s in strategies}
    matrix = {}
    for a, b in combinations(strategies, 2):
        sa = sb = 0
        for _ in range(games):
            x, y = play_match(a, b, rng, rounds)
            sa += x
            sb += y
        matrix[(a.name, b.name)] = sa
        matrix[(b.name, a.name)] = sb
        totals[a.name] += sa
        totals[b.name] += sb
    return totals, matrix


def make_rng(seed):
    return random.Random(seed)
