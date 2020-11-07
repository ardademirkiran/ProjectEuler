def isprime(a):
 ret = ""
 for o in range(2,a):
  if a%o== 0:
   ret = "asal değil"
   break
  elif o == a-1:
   ret = "asal"
 return ret

kume = [2,3,5]
for i in range(7,200000):
 if isprime(i) == "asal":
  kume.append(i)
 if len(kume) == 10001:
  break

print(kume[len(kume)-1])


