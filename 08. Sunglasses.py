n = int(input())
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

