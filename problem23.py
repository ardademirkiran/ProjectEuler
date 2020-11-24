def isAbundant(num):
    divs = []
    for x in range(1,int(num/2)+1):
        if num%x == 0:
            divs.append(x)
    if sum(divs)>num:
        return 1
    else:
        return 0
abundants = set()
set1_w = set()
answer_l = set([y for y in range(1,28124)])
for number in range(1,28124):
    if isAbundant(number) == 1:
        abundants.add(number)
for a in abundants:
    for b in abundants:
        set1_w.add(a+b)

answer_l = answer_l - set1_w
print(sum(answer_l))
