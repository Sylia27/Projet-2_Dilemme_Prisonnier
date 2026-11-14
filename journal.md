# Journal
## Partie 1
### Le protocole:

Nombre de tours : 200 \
Nombre de parties : 5  \
Format : tournoi tous contre tous, chaque paire de stratégies distinctes joue une fois 5 parties de 200 tours.\
**Valeurs des paramétres :** \
Matrice de gains : donné dans l'énoncé \
Graine : 27 (paramétrable)\
Ordre des stratégies: ALL-D, RANDOM, TIT-FOR-TAT, TESTER, JOSS\
**Paramétres propres aux stratégies:**\
ALL-D: aucun paramètre elle joue toujours D \
RANDOM: probabilité de jouer C = 0,5 (on tire rng.random si < 0,5 elle joue C, sinon D)\
JOSS : probabilité de remplacer C par D = 0,1 (une fois sur 10) .Elle calcule d'abord le coup de TFT,si c'est C elle tire rng.random et joue D si le nombre est < 0,1. Si TFT aurait joué D, elle joue D sans tirage.Le test s'applique aussi au tour 1.\
TIT-FOR-TAT: premier coup C, puis à chaque tour elle rejoue le dernier coup de l'adversaire (opp[-1])\
TESTER: tour 1 = D (provocation)puis tour 2 = C (on observe la réaction). Si l'adversaire a joué D au tour 2(riposte)  TESTER joue comme TIT-FOR-TAT ensuite. Sinon il répète C, C, D (un D tous les trois tours à partir du tour 4)\
 **Résultats :**
 ![Capture d'écran qui montre le classement de la 1ére partie](Result_part_1.png)



