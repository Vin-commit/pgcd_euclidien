#!/usr/bin/python3
# coding: utf-8


# Peut se s’exécuter ainsi : 
# ./<nom du fichier script Python> après “chmod 700 <nom du fichier script Python>”
#
# Propriétés mathématiques utilisées :
# -----------------------------------------------
#
# si a < b, alors pgcd (a, b) = pgcd (a, b%a)
# si a > b, alors pgcd (a, b) = pgcd (a%b, b)
# Si l’on veut ppcm(a, b) → utilisez ppcm(a, b) = a*b/pgcd(a, b).
   
def pgcd_euclidien (a, b):
  while (a*b != 0): # ou (a*b > 0) 
    if (a > b):
      a = a % b
    else:
      b = b % a
  if (a == 0):
    return b
  else:
    return a


a = int(input(“Entrez le premier nombre : ”))
b = int(input(“Entrez le second nombre : ”))
print (“Leur pgcd est :”, pgcd_euclidien (a, b)) 


------------------------------------------------------------------------ Résultat --------------------------------------------------------------------------
 scrot.png