import random
from itertools import combinations

PAYOFF = {("C", "C"): (3, 3), ("C", "D"): (0, 5),
          ("D", "C"): (5, 0), ("D", "D"): (2, 2)}


def flip(move):
    """Renvoie le coup opposé (utilisé par le bruit)."""
    return "D" if move == "C" else "C"


def play_match(s1, s2, rng, rounds=200, noise=0.0, w=None):
    """Joue UNE partie. Renvoie (score1, score2).
    noise : probabilité que chaque coup soit inversé (0 = pas de bruit)
    w     : si donné, la partie continue après chaque tour avec probabilité w
            (horizon inconnu) ; sinon elle dure exactement `rounds` tours."""
    h1, h2 = [], []
    sc1 = sc2 = 0
    t = 0
    while True:
        m1 = s1.play(h1, h2, rng)
        m2 = s2.play(h2, h1, rng)

        if noise > 0:                      # MODIFICATION A : bruit
            if rng.random() < noise:
                m1 = flip(m1)
            if rng.random() < noise:
                m2 = flip(m2)

        g1, g2 = PAYOFF[(m1, m2)]
        sc1 += g1
        sc2 += g2
        h1.append(m1)
        h2.append(m2)
        t += 1

        if w is None:                      # durée fixe (étapes 1 et 2)
            if t >= rounds:
                break
        elif rng.random() >= w:            # MODIFICATION B : horizon inconnu
            break
    return sc1, sc2


def tournament(strategies, rng, games=5, rounds=200, noise=0.0, w=None):
    totals = {s.name: 0 for s in strategies}
    matrix = {}
    for a, b in combinations(strategies, 2):
        sa = sb = 0
        for _ in range(games):
            x, y = play_match(a, b, rng, rounds, noise, w)
            sa += x
            sb += y
        matrix[(a.name, b.name)] = sa
        matrix[(b.name, a.name)] = sb
        totals[a.name] += sa
        totals[b.name] += sb
    return totals, matrix


def make_rng(seed):
    return random.Random(seed)