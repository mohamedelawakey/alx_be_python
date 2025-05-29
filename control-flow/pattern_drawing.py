size_of_pattern = int(input('Enter the size of the pattern: '))

i = 0

while i < size_of_pattern:
    x = 0
    while x < size_of_pattern:
        print('*',end='')
        x += 1
    print()
    i += 1

"""

for i in range(size_of_pattern):
    for x in range(size_of_pattern):
        print('*',end='')
    print()
    
"""