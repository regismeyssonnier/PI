# -*- coding: latin-1 -*-
from decimal import Decimal, getcontext

def pi_ramanujan(n_terms=5, precision=100):
    """
    Calcule pi en utilisant la série de Ramanujan.
    
    n_terms : nombre de termes de la série à sommer
    precision : nombre de décimales de précision
    """
    getcontext().prec = precision + 10  # un peu plus pour compenser les erreurs d'arrondi
    
    total = Decimal(0)
    for k in range(n_terms):
        # Calcul du terme
        num = Decimal(factorial(4*k)) * (Decimal(1103) + Decimal(26390)*k)
        den = (Decimal(factorial(k)) ** 4) * (Decimal(396) ** (4*k))
        term = num / den
        total += term
        if k % 100 == 0:
            print(k)

    constant = Decimal(2).sqrt() * Decimal(2) / Decimal(9801)
    pi_inv = constant * total
    pi = 1 / pi_inv
    return +pi  # le + force l'arrondi selon la précision

def pi_chudno_bro(n_terms = 5, precision = 100):

    getcontext().prec = precision + 10

    total = Decimal(0)
    for k in range(n_terms):
        num = Decimal(-1)**k * Decimal(factorial(6 * k)) * (Decimal(13591409) + Decimal(545140134) * k)
        den = Decimal(factorial(3*k)) * (Decimal(factorial(k))**3) * (Decimal(640320) ** Decimal(3*k+3/2))
        total += num / den

    pi_inv = 12 * total
    pi = 1 / pi_inv

    return +pi

def factorial(n):
    """Factorielle en Decimal pour très grands nombres"""
    if n == 0 or n == 1:
        return Decimal(1)
    f = Decimal(1)
    for i in range(2, n+1):
        f *= Decimal(i)
    return f

# Exemple d'utilisation
print(pi_ramanujan(n_terms=125000, precision=1000000))
#print(pi_chudno_bro(n_terms=125, precision=1000))
