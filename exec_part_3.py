"""Étape 3 : modifications du tournoi (7 stratégies de l'étape 2).
Usage : python exec_part_3.py --seed 27 --noise 0.05
        python exec_part_3.py --seed 27 --w 0.9
"""
import argparse
from moteur_2 import tournament, make_rng
from strat import STRATS_ETENDU


def afficher(totals, matrix, names):
    print("\nCLASSEMENT")
    classement = sorted(totals.items(), key=lambda x: -x[1])
    for rang, (nom, score) in enumerate(classement, 1):
        print(f"{rang}. {nom:<18} {score}")

    print("\nMATRICE (score de la ligne contre la colonne)")
    print(" " * 19 + "".join(f"{n:>18}" for n in names))
    for a in names:
        ligne = "".join(f"{matrix.get((a, b), '-'):>18}" for b in names)
        print(f"{a:<19}{ligne}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--noise", type=float, default=0.0,
                        help="probabilité d'inversion de chaque coup (ex. 0.05)")
    parser.add_argument("--w", type=float, default=None,
                        help="probabilité de continuer après chaque tour (ex. 0.9)")
    args = parser.parse_args()

    strats = [c() for c in STRATS_ETENDU]
    rng = make_rng(args.seed)
    totals, matrix = tournament(strats, rng, games=5, rounds=200,
                                noise=args.noise, w=args.w)

    print(f"seed = {args.seed}   bruit = {args.noise}   w = {args.w}")
    afficher(totals, matrix, [s.name for s in strats])