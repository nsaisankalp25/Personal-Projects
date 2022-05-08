while True:
    print('------------')
    num = input('Enter Starting number: ')
    num = int(num)
    while True:
        if num == 1:
            break

        elif num%2 == 0:
            # even number
            go = num/2
            print(int(go))
            num = go
            continue
        else:
            go = (num*3)+1
            print(int(go))
            num = go
            continue
    print('Done.')
    yrn = input('Want to continue? [y/n] ')
    if yrn.lower() == 'y' or yrn.lower() == 'yes':
        continue
    else:
        break