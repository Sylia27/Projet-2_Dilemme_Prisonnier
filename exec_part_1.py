
import argparse
from moteur import tournament, make_rng
from strat import STRATS


def afficher(totals, matrix, names):
    print("\nCLASSEMENT")
    classement = sorted(totals.items(), key=lambda x: -x[1])
    for rang, (nom, score) in enumerate(classement, 1):
        print(f"{rang}. {nom:<12} {score}")

    print("\nMATRICE (score de la ligne contre la colonne)")
    print(" " * 13 + "".join(f"{n:>13}" for n in names))
    for a in names:
        ligne = "".join(f"{matrix.get((a, b), '-'):>13}" for b in names)
        print(f"{a:<13}{ligne}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=27)
    args = parser.parse_args()

    strats = [c() for c in STRATS]          
    rng = make_rng(args.seed)             
    totals, matrix = tournament(strats, rng, games=5, rounds=200)

    print(f"seed = {args.seed}")
    afficher(totals, matrix, [s.name for s in strats])