import functools

def OuterMethod():
    print("Outer Method Stuff")

    def InnerMethod1():
        print("Inner 1")

    def InnerMethod2():
        print("Inner 2")
    
    InnerMethod1()
    InnerMethod2()

OuterMethod()

def Shalom(name):
    print("Shalom", name , "!")

def greet_ShalomMan(shalomFunc):
    return shalomFunc("ShalomMan") # This function returns another function with a string as input parameter

# Functions are treated as first class objects, which are objects that can be passed in as parameters
    # like ints and strings and collections
    # Dont pass in the () when passing in the method, This is known as referencing the method
    # Method() invokes the method, while just Method passes a reference to the method
greet_ShalomMan(Shalom)

# Simple Decorators: A reference variable holds a reference to a method
def myDecorator(functionParameter):
    def wrapper():
        print("Before functionParameter called")
        functionParameter()
        functionParameter()
        functionParameter()
        print("After functionParameter called")
    return wrapper # Note: The reference to the wrapper function is being returned

@myDecorator
def say_yeet():
    print("YEET")

#YEET = myDecorator(say_yeet) # This is what the @myDecorator does
# Stored the function into variable YEET
#YEET() 

standardYeet = say_yeet()

# Need to use @functools for decorators which needs to be imported
def decorators2(functionParameter):
    @functools.wraps(functionParameter) # Decorators need this to allow the functionParameter to retain its identity
    def wrapper_do_twice(*args, **kwargs):
        return functionParameter(*args, **kwargs)  # Returns whatever the passed in functionParameter returns
    return wrapper_do_twice

# When parameters are *args, **kwargs, these allow the functionParameter that is passed in
# contain an arbitrary amount of parameters of arguments and keyword arguments

@decorators2
def say_dab(name):
    print(name, "dabs!")

@decorators2
def worldoftanks(tank):
    print(tank, "rolls out!")
    return tank

dabber1 = say_dab("Shalom man")
tanker1 = worldoftanks("Tiger 2")
print(tanker1)
# Returning values from Decorated Functions

# The Standard for Simple Decorators (Template)
def StandardDecorator(functionParameter):
    @functools.wraps(functionParameter)
    def wrapper_decorator(*args, **kwargs):
        # DO SOMETHING BEFORE
        value = functionParameter(*args, **kwargs)
        # DO SOMETHING AFTER
        return value
    return wrapper_decorator


# Fancy Decorators
