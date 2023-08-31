# 08. Sunglasss

n = int(input())
# First Way
# print('*' * (2 * n), end='')
# print(' ' * (n), end='')
# print('*' * (2 * n))
# for row in range(n - 2):
#     print('*////////*')
#     if row == (n - 1) // 2 - 1:
#         print('|' * n, end='')
#     else:
#         print(' ' * n, end='')
#     print('*////////*')
            
# print('*'*(2 * n), end='')
# print(' '*(n), end='')
# print('*'*(2 * n))

# Second Way
stars = 2 * n
space = 5 * n - 4 * n 
slash = 2 * n-2
is_n_even =  n % 2 == 0

print('*'*stars + ' '*space + '*'*stars)

for row in range(1, (n - 2)+1):
    if row == n//2 and not is_n_even:
        print('*' + '/'*slash + '*' + '|'*space + '*' + '/'*slash + '*')
    elif is_n_even and row == (n // 2) - 1:           
        print('*' + '/'*slash + '*' + ' '*space + '*' + '/'*slash + '*')

print('*'*stars + ' '*space + '*'*stars)
    
