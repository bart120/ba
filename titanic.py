import csv

fichier = open('titanic.csv', 'r')
#contenu = fichier.readlines()
#for ligne in contenu:
#    tab_ligne = ligne.split(';')
#    print(tab_ligne[1])

def retourner_name(passager):
    return passager['Name']

def retourner_sexe_age(passager):
    return passager['Sex']+passager['Age']

contenu = csv.DictReader(fichier, delimiter=';')
passagers = list(contenu)
passagers.sort(key=retourner_sexe_age, reverse=True)
for personne in passagers:
    #print("{} avec le ticket {}".format(personne['Name'], personne['Ticket']))
    print(personne)
#nbr_femme = passagers.count({'Sex': 'female'})

nbr_femme = sum(personne['Sex']=='female' for personne in passagers)
print(nbr_femme)

hommes = sum(personne['Sex']=='male' and personne['Survived']=='1' 
             and int(personne['Age']) >= 50 for personne in passagers)
print(hommes)

femmes = []
for personne in passagers:
    if(personne['Sex'] == 'female'):
        femmes.append(personne)
print(femmes)

for personne in passagers:
    if(personne['Survived'] == '1'):
        personne['Survived'] = '0'
print (passagers)



