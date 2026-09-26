# les nombre premier 
# sol1
import time

import math 


def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

#sol2
def est_premier2(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# sol3 

def est_premier3(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False

n=1000000007
start = time.time()
print(est_premier(n))
end = time.time()
print(f"Temps d'exécution (sol1): {end - start} secondes")

start = time.time()
print(est_premier2(n))
end = time.time()
print(f"Temps d'exécution (sol2): {end - start} secondes")

start = time.time()
print(est_premier3(n))
end = time.time()
print(f"Temps d'exécution (sol3): {end - start} secondes")
