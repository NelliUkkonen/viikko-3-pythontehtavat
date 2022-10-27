import math

luku = (input("Anna lukuja, erottele luvut pilkulla: "))

ls = luku.split(",") 
print(ls)

pienin = min(ls)
suurin = max(ls)
summa = sum(ls)

print(pienin)
print(suurin)