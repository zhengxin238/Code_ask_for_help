from pref_voting.profiles_with_ties import Ranking
r = Ranking({0:2, 1:1, 2:3})
print(r)
r.display()
print()

r = Ranking({0:1, 1:1, 2:3})
print(r)
r.display()

print()
r = Ranking({0:1,  2:3})
print(r)
r.display()