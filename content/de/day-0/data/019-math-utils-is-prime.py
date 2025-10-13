## math-utils-is-prime
def ist_primzahl(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

from math_utils import ist_primzahl
print(ist_primzahl(7))
