# Python Classes: Instance and Inheritance

x = "Dog"

class A:
    x = "Cat"

class B(A):

    x = "Ferret"
    
    def __init__(self, x):
        self.x = x # If no passed in parameter, would look for x value in the scope its defined in

class C(B):
    x = "Fish"
    def __init__(self):
        pass

a = A()
print(a.x)
print(x)

b = B("Shalom")
print(b.x)

print("===================")

class Bar():
    def __init__(self, value):
        self.value = value

    def increment(self):
        print("SUPER CLASS IMPLEMENT")
    
    def double_incremented(self):
        self.increment()
        self.increment()
        self.increment()
        self.increment()

class Foo(Bar):
    value = 100
    def __init__(self, value): 
        Bar.__init__(self, value) # Takes in the super class initializer (Constructor)
        self.value = self.value * Foo.value # Foo.value already predefined

    def increment(this):
        this.value += 10

class Gorp(Bar):
    delta = 100
    def increment(self):
        self.value += self.delta

f = Foo(0)
print(f.value)

f.double_incremented() # Calls the superclass method but inside the method it calls for the increment
    # Method that exists in both the superclass and subclass, but begins search the subclass first for
    # the name of this method
print(f.value)



