# trouver rouver deux nombres dont la somme vaut 9: [2, 7, 11, 15, 3, 6]

import time
import random
#9-2=7
#find(7)
#deux nombres sont 2 et 7

# deuxieme cas : 9-1=8
#find(8)
#passer pour element suivant 9-2=7 et sercher 


def isnumbreinlist(n, lst):
    for i in lst:
        if i == n:
            return True
    return False

def find_townumbresome9(lst):
    for i in lst:
        complement = 9 - i
        if complement>=0 and  isnumbreinlist(complement, lst):
            return (i, complement)
    return None
l = [
   random.randint(10**18, 10**30)
    for _ in range(100_000)
]

# On ajoute notre paire recherchée
l[50000] = 3
l[80000] = 6


start_time = time.time()
l.sort()
result = find_townumbresome9(l)
end_time = time.time()

print("Result:", result)
print("Execution time:", end_time - start_time)