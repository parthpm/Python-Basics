def askint():
    try:
        val = int(input("Please enter an integer: "))
    except:
        print("Looks like you did not enter an integer!")

    finally:
        print("Finally, I executed!")
        print (val)    #it has to be in finally block otherwise local variable 'val' referenced before assignment

askint()
#Notice how we got an error when trying to print val (because it was never properly assigned)
# Lets remedy this by asking the user and checking to make sure the input type is an integer:
print('\n\n')
def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print ("Looks like you did not enter an integer!")
            continue
        else:
            print ('Yep thats an integer!')
            break
        finally:
            print ("Finally, I executed!")
        print (val)

askint()
