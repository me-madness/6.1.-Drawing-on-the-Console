import math

n = int(input())
stars = 1
if stars % 2 == 0:
    stars += 1
    
roof_leght = math.ceil(n / 2)
for i in range(roof_leght):
    padding_roof = (n - stars) // 2
    line = '-' * padding_roof \
          + '*' * stars \
          + '-' * padding_roof
    print(line) 
    stars += 2
    
           
