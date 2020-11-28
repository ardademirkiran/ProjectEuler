def isPrime(num):
    if num == 0 or num == 1 or num <= 0:
        return 0
    elif num == 2:
        return 1
    else:
        for x in range(2,int(num**0.5)+1):
            if num%x == 0:
                return 0
    return 1
def formula(num1,num2):
    prime_counter = 0
    for n in range(0,10000):
        form = n**2 + num1*n + num2
        if isPrime(form) == 1:
            prime_counter += 1
        else:
            break
    return prime_counter
answer_ref = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        formul = formula(a,b)
        if formul > answer_ref:
            answer_ref = formul
            a_ref = a
            b_ref = b
            prime_counter = formul
            answer = a*b
print("a = {}\nb = {}\nPrime counter: {}\nAnswer:\t{}".format(a_ref,b_ref,prime_counter,answer))
 

