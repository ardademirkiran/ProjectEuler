def isCom(num1,num2):
    for let1 in str(num1):
        if let1 in str(num2):
            return let1
    return 0
def r_com(num1,num2,com):
    num1_s = str(num1)
    num2_s = str(num2)
    num1_s = num1_s.replace(com,"")
    num2_s = num2_s.replace(com,"")
    num1_s = int(num1_s)
    num2_s = int(num2_s)
    if num1_s/num2_s == num1/num2:
        return num1/num2
    else:
        return 0

denoms = 1
noms = 1

for denominator in range(10,100):
    if denominator % 10 != 0 and denominator % 11 != 0:
        for numerator in range(10,denominator):
            if numerator % 10 != 0 and numerator % 11 != 0 and numerator != denominator:
                iscom = isCom(numerator,denominator)
                if iscom == 0:
                    continue
                else:
                    rcom = r_com(numerator,denominator,iscom)
                    if rcom == 0:
                        continue
                    else:
                        denoms *= denominator
                        noms *= numerator
            else:
                continue
    else:
        continue

print("Answer:\t" ,int(denoms/noms))
