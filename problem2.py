list1 = [1,2]
i = 0
toplam = 0
while (list1[i]<4000000):
 list1.append(list1[i]+list1[i+1])
 i+=1
for x in list1:
 if x%2==0:
  toplam+=x
print(toplam)

 
