rows = 10
for i in range(rows):
    for j in range(rows - i - 1):
        print(' ', end='')
    if i == rows - 1:
        for j in range(2 * rows - 1):
            print('*', end='')
    else:
        for j in range(2 * i + 1):
            if j == 0 or j == 2 * i:
                print('*', end='')
            else:
                print(' ', end='')
    print()
