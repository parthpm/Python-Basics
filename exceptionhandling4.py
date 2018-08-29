def pow():
    while True:
        try:
            t=input('Enter the no for square: ')

        except TypeError:
            print("typeerror , exception caught")
            continue
        else:
            print('No exception caught')

        print("Square of {} is {}".format(t, t ** 2))
        break
pow()