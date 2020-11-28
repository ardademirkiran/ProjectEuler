from itertools import permutations
numbers = list(permutations(range(10)))
numbers.sort()
print(*numbers[999999],sep="")
      
