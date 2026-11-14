# Projet-2_Dilemme_Prisonnier



## Relancer le tournoi de l'étape 1
python run_step_1.py --seed 27
## Relancer le tournoi de l'étape 2
python run_step_2.py --seed 27
## Relancer le tournoi de l'étape 3
- Pour lancer avec le bruit:
python exec_part_3.py --seed 27 --noise 0.05
- Pour lancer avec horizon inconnu :
python exec_part_3.py --seed 27 --w 0.95
## Fichiers
- strat.py : les stratégies
- moteur.py : une partie et le tournoi
- moteur_2.py : moteur pour la partie 3 
- exec_step_1.py : lance l'étape 1
- exec_step_2.py : lance l'étape 2
- exec_step_3.py : lance l'étape 3
- journal.md : journal de bord