fib = [1,1,2]
while True:
    new = fib[len(fib)-1] + fib[len(fib)-2]
    if len(str(new)) == 1000:
        fib.append(new)
        print(len(fib))
        break
    fib.append(new)


    

