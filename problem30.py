def isProper(num):
    num = str(num)
    sum_ = 0
    for digit in num:
        sum_ += int(digit)**5
    if sum_ == int(num):
        return 1
    else:
        return 0
limit = (9**5)*4
answer = 0
for number in range(1,limit):
    if isProper(number) == 1:
        answer += number
        print(number , "limit = ",limit)
print(answer-1)