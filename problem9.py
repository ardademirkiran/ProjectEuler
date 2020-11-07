for x in range(1,1000):
 for y in range(1,1000):
  kare_top = (x**2)+(y**2)
  if (kare_top**0.5)+x+y == 1000:
   print(x*y*kare_top**0.5)
