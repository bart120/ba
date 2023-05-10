##t = 34, 67, 9, 6, 904, 6
##print(t[4])
##
##index = 0
##while index <= len(t)-1:
##    print(t[index])
##    index += 1
##    #index = index + 1
##
##for n in t:
##    print(n)

def est_dans_tableau(tableau, element_a_trouver):
    for element in tableau:
        if element == element_a_trouver:
            return True
    return False

fruits = ['kiwi', 'mangue', 'orange']

#for f in fruits:
#    print(f)
fruits.append('pomme')
fruits.append('prune')
for i in range(3, 5):
    print(fruits[i])
for i in range(0, 5):
    nouveau_fruit = input('Nouveau fruit {} ?'.format(i+1))
    if(est_dans_tableau(fruits, nouveau_fruit)):
        print("Le fruit {} est déjà connu.".format(nouveau_fruit))
    else:
        fruits.append(nouveau_fruit)
fruits.sort()
print(fruits)
    
