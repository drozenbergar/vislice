# Napiši program, ki izpiše vsa praštevila manjša od 200

def je_praštevilo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for x in range(2, 201):
    if je_praštevilo(x):
        print(x)
