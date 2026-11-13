"""Stratégies du dilemme du prisonnier itéré.

Une stratégie est un objet avec :
  - name : son nom
  - play(own, opp, rng) -> "C" ou "D"
      own :liste de MES coups passés
      opp :liste des coups passés de l'ADVERSAIRE
      rng :générateur aléatoire partagé (pour la graine fixe)
Le tour courant est len(own) 
"""

C, D = "C", "D"


class Strategy:
    """toute stratégie a un nom et une méthode play"""
    name = "BASE"

    def play(self, own, opp, rng):
        raise NotImplementedError


class AllD(Strategy):
    """Toujours D."""
    name = "ALL-D"

    def play(self, own, opp, rng):
        return D


class Random(Strategy):
    """C ou D au hasard"""
    name = "RANDOM"

    def play(self, own, opp, rng):
        return C if rng.random() < 0.5 else D


class TitForTat(Strategy):
    """C au premier tour puis copie le dernier coup de l'adversaire."""
    name = "TIT-FOR-TAT"

    def play(self, own, opp, rng):
        return C if not opp else opp[-1]


class Tester(Strategy):
    """D au tour 1, C au tour 2 
    Si l'adversaire a riposté D au tour 2: TIT-FOR-TAT ensuite.
    Sinon on répète C, C, D"""
    name = "TESTER"

    def play(self, own, opp, rng):
        t = len(own)              # numéro du tour, à partir de 0
        if t == 0:
            return D
        if t == 1:
            return C
        if opp[1] == D:           # il a riposté à ma provocation
            return opp[-1]        # on joue comme TIT-FOR-TAT
        return D if (t - 1) % 3 == 2 else C #D un tour sur trois


class Joss(Strategy):
    """TIT-FOR-TAT, mais remplace C par D une fois sur dix."""
    name = "JOSS"

    def __init__(self, p_defect=0.1):
        self.p = p_defect

    def play(self, own, opp, rng):
        move = C if not opp else opp[-1]
        if move == C and rng.random() < self.p:
            return D
        return move



STRATS = [AllD, Random, TitForTat, Tester, Joss]