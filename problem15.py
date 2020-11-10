def fact(num):
 res = 1
 for x in range(1,num+1):
  res *= x
 return res

print(int(fact(40)/(fact(20)**2)))
  
