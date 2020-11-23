num_dict =  {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

answer = 0

with open("names.txt","r") as file_:
    n_list =[]
    text = file_.read()
    text_l = text.split(",")
    for word in text_l:
         word = word.strip('"')
         n_list.append(word)
    n_list.sort()
    enum_list = enumerate(n_list,1)
    for n_word in enum_list:
        sum_ = 0
        res = 0
        for letter in n_word[1]:
            sum_+=num_dict[letter]
        res = sum_ * n_word[0]
        answer += res
    print(answer)
            

    