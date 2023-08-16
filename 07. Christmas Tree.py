# 07. Christmas Tree

n = int(input())
# First Way
for row in range(n+1):
    stars = '*'*row
    spaces = ' '*(n-row)
    print(spaces, end='')   
    print(stars, end='')
    print('|', end='')   
    print(stars, end='')
    print(spaces)
    
# Second Way
print(' '*(n + 1) + '|')
for row in range(n+1):
        print(' '*(n-row) + '*'*row + ' ' + '|' + ' ' + '*'*row )