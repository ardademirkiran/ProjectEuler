def hmDivisor(num):
 divisors = []
 divisors1 = []
 for y in range(1,int(num**0.5)+1):
  if num%y == 0 and y not in divisors:
   divisors.append(y)
 for a in divisors:
  for b in divisors:
   if (a*b) not in divisors1 and num%(a*b) == 0:
    divisors1.append(a*b)
 return len(divisors1)
 
for x in range(1,1000000):
 tri_x = (x*(x+1))/2
 print(int(tri_x))
 if hmDivisor(tri_x) > 500:
  print("Answer:\t{} \n".format(int(tri_x)))
  break
