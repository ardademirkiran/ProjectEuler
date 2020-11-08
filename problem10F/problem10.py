def isPrime(num):
 if num%2 == 0:
  return 0
 for x in range(3,int(num**0.5)+1,2):
  if num%x == 0:
   return 0

 return 1
sum = 0

for i in range(3,2000000):
 if isPrime(i) == 1:
  print(i)
  sum += i

print(sum+2)
 
 
