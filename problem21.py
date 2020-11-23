def fsum_divs(x):
    divs_list = []
    for num in range(1,(int(x/2)+1)):
        if (x%num) == 0:
            divs_list.append(num)
    return sum(divs_list)
res_set = set()
for number in range(1,10000):
    c_num = fsum_divs(number)
    ref_num = fsum_divs(c_num)
    if number == ref_num and ref_num < 10000 and c_num != number:
        print(number)
        res_set.add(number)
print(sum(res_set))
    

    

        
 