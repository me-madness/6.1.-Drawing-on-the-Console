n = int(input())
print(('+ ' + '- '*(n-2) + '+ '))
for row in range(n):
    print('| ' + '- '*(n-2) + '|')
print(('+ ' + '- '*(n-2) + '+ '))