from moteur import play_match, make_rng, PAYOFF
from strat import TitForTat, AllD

rng = make_rng(42)
s1, s2 = TitForTat(), AllD()
h1, h2 = [], []

print("tour | TFT | ALL-D | gain TFT | gain ALL-D")
for t in range(1, 11):
    m1 = s1.play(h1, h2, rng)
    m2 = s2.play(h2, h1, rng)
    g1, g2 = PAYOFF[(m1, m2)]
    h1.append(m1)
    h2.append(m2)
    print(f"{t:>4} |  {m1}  |   {m2}   |    {g1}     |    {g2}")

print()
print("Score via play_match :", play_match(TitForTat(), AllD(), make_rng(42), rounds=10))