liste = set([])
sayi = 0
for x in range(999,100,-1):
 for y in range(999,100,-1):
  pal = str(x*y)
  if pal == pal[: :-1]:
   liste.add(pal)
for i in liste:
 if len(i) == 6 and i.startswith("9"):
  print(i)

  
