liste = [] # création d'une liste vide
for i in range(0, 5):
    liste.append(i)
print(liste) # affiche [0, 1, 2, 3, 4]
del(liste[2]) # supprime l'élément de rang 2 dans la liste
print(liste) # affiche [0, 1, 3, 4]
liste.remove(3) # supprime la valeur 3 de la liste
print(liste) 