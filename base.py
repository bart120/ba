#fonction est_pair
def est_pair(nombre):
  test = nombre % 2 == 0
  return test


num = 16
if(est_pair(num)):
    print("{} est un nombre pair".format(num))
else:
    print("{} est un nombre impair".format(num))
