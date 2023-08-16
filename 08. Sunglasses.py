# 08. Sunglasss

n = int(input())
# First Way
print('*' * (2 * n), end='')
print(' ' * (n), end='')
print('*' * (2 * n))
for row in range(n - 2):
    print('*////////*')
    if row == (n - 1) // 2 - 1:
        print('|' * n, end='')
    else:
        print(' ' * n, end='')
    print('*////////*')
            
print('*'*(2 * n), end='')
print(' '*(n), end='')
print('*'*(2 * n))

# Second Way
stars = 2 * n
space = 5 * n - 4 * n 
slash = 2 * n-2

print('*'*stars + ' '*stars + '*'*stars)

for row in range(n - 2):
    print('*' + '/'*slash + '*' + ' '*space + '*' + '/'*slash + '*')
