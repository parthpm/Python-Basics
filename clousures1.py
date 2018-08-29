#A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
#As observed below, closures help to invoke function outside their scope.
#The function innerFunction has its scope only inside the outerFunction.
#But with the use of closures we can easily extend its scope to invoke a function outside its scope.

def outerfunc(value1):
    greeting=value1

    def enclosingfunc(value2):
        print(value1+value2)

    return enclosingfunc

p=outerfunc('Hello')
print(p) # p=enclosingfunction
p(' Parth') # p remembers what was passed to outer function that is greeting
del outerfunc
#even after deleting
p('Maheshwari')

#When and why to use Closures:
#1.As closures are used as callback functions, they provide some sort of data hiding.
# This helps us to reduce the use of global variables.

#2.hen we have few functions in our code, closures prove to be efficient way.
#  But if we need to have many functions,  then go for class (OOP).
