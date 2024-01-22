from itertools import islice, count
print(sum(p for p in islice((i for i in count(2) if all(i%j!=0 for j in range(2,int(i**0.5)+1))),1000000)))
