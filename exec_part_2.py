"""Étape 2 : tournoi avec les 5 stratégies du cours + GRIM + TIT-FOR-TWO-TATS
Mêmes paramètres qu'à l'étape 1 (5 parties de 200 tours, graine 42).
Usage : python exec_part_2.py --seed 42
        
"""
import argparse
from moteur import tournament, make_rng
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
    
    args = parser.parse_args()

    strats = [c() for c in STRATS_ETENDU ]
    rng = make_rng(args.seed)
    totals, matrix = tournament(strats, rng, games=5, rounds=200)

    print(f"seed = {args.seed}   stratégies = {len(strats)}")
    afficher(totals, matrix, [s.name for s in strats])