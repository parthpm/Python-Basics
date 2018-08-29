for l in range(1,101):
    if l%3==0 and l%5==0:
        print("FIZZBUZZ")

    elif   l%3==0:
        print("FIZZ")
    elif l%5==0:
        print("BUZZ")

    else:
        print(l)