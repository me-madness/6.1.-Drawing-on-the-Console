n = int(input())
for row in range(n+1):
    stars = '*'*row
    spaces = ' '*(n-row)
    print(spaces, end='')   
    print(stars, end='')
    print('|', end='')   
    print(stars, end='')
    print(spaces)