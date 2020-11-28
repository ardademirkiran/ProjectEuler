def factorial(num):
    if num == 1 or num == 0:
        return 1
    ret = 1
    for x in range(1,num+1):
        ret*=x
    return ret

def isProper(num):
    sum_ = 0
    num = str(num)
    for digit in num:
        sum_ += factorial(int(digit))
    if sum_ == int(num):
        return 1
    else:
        return 0
answer = 0
for number in range (10,50000):
    if isProper(number) == 1:
        answer+=number
        print("Proper number:\t ",number)
    else:
        continue
print("Answer:\t",answer)

