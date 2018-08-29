x = 25

def printer():
    x = 50
    return x

print (x)
print (printer())


''' Priority Rule LEGB
L: Local — Names assigned in any way within a function (def or lambda)), and not declared global in that function.

E: Enclosing function locals — Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer.

G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.

B: Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError,...
'''

#Local
def square(x):
    return x**2

#enclosing function calls

str='hello this is global statement'

def g():
    name='Sameer'

    def h():
        name='Parth'
        print('hello' + name)
    h()

g()


#local variables
x = 50

def func(x):
    print ('x is', x)
    x = 2
    print ('Changed local x to', x)

func(x)
print ('x is still', x)

#Global keyword

x = 50

def func():
    global x
    print ('This function is now using the global x!')
    print ('Because of global x is: ', x)
    x = 2
    print ('Ran func(), changed global x to', x)

print ('Before calling func(), x is: ', x)
func()
print ('Value of x (outside of func()) is: ', x)