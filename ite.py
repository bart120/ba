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

fruits = ['kiwi', 'mangue', 'orange']

#for f in fruits:
#    print(f)
fruits.append('pomme')
fruits.append('prune')
for i in range(3, 5):
    print(fruits[i])
for i in range(0, 5):
    nouveau_fruit = input('Nouveau fruit {} ?'.format(i+1))
    test = False
    for element in fruits:
        if element == nouveau_fruit:
            print("Le fruit {} est déjà connu.".format(nouveau_fruit))
            test = True
    if(test == False)
        fruits.append(nouveau_fruit)
print(fruits)
    
