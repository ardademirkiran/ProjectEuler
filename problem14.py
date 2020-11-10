def collatz(num):
 if num%2 == 0:
  return num/2
 else:
  return ((3*num)  + 1)

len_liste = 0
for x in range(1000000,1,-1):
 sayi = x
 liste = []
 
 while (sayi != 1):
  liste.append(sayi)
  sayi = collatz(sayi)
 if len(liste) > len_liste:
  len_liste = len(liste)
  print(x)
  ext = x

print("Answer:\t{}".format(ext))


 
 
