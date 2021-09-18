
class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        try:
            poppedElement = self.data[-1]
            self.data.pop()
            return poppedElement
        except:
            return None
    
    def read(self):
        try:
            return self.data[-1]
        except:
            return None
    
    def display(self):
        print(self.data)

aStack = Stack()
aStack.push(1)
aStack.push(2)
aStack.push(3)
aStack.push(4)
aStack.display()
aStack.pop()
aStack.display()
print(aStack.read())

# Syntax Checker for Opened and Closed Braces
class Linter:
    def __init__(self):
        self.stack = Stack()
    
    def lint(self, text):
        for character in text:
            if character == "{" or character == "(" or character == "[":
                self.stack.push(character)
            elif character == "}" or character == ")" or character == "]":
                popped_opening_brace = self.stack.pop()

                if popped_opening_brace == None:
                    return f"{character} doesn't have an opening brace"
                elif popped_opening_brace == "{" and character == "}" or popped_opening_brace == "[" and character == "]" or popped_opening_brace == "(" and character == ")":
                    continue
                else:
                    return f"{character} is mismatched opening brace"
                
        if self.stack.read() != None:
            return f"{self.stack.read()} does not have a closing brace"

        return "No Errors Found"

lints = Linter()
code = "[]( var x = { y: 1, 2, 3 } )"
answer = lints.lint(code)
print(answer)



class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
    
    def dequeue(self):
        try:
            frontElement = self.queue[0]
            self.queue.pop(0)
            return frontElement
        except:
            return None
    
    def read(self):
        try:
            return self.queue[0]
        except:
            return None
    
    def display(self):
        print(self.queue)
    
# Printing Manager
class PrintManager:
    def __init__(self):
        self.queue = Queue()
    
    def QueuePrintJob(self, document): # For now these are string statements
        self.queue.enqueue(document)
    
    def Run(self):
        while self.queue.read(): # Keeps running the loop as until it reads None
            print(self.queue.dequeue())
    
printer = PrintManager()
printer.QueuePrintJob("SHALOM")
printer.QueuePrintJob("faafqwefw")
printer.QueuePrintJob("SHAfwefewfLOM")
printer.QueuePrintJob("222")
printer.QueuePrintJob("SHAfasdaLOM")
printer.QueuePrintJob("dawdwwwwww")
printer.Run()

# Exercise 1: Queue
# Exercise 2: 4

# Exercise 3: 3

# Exercise 4
# Function uses a Stack to reverse a string

def reverseStringStack(string):
    stacklord = Stack()
    reversedString = ""
    for character in string:
        stacklord.push(character)
    
    while stacklord.read(): # Runs until there None remains within the stack
        reversedString += stacklord.pop() # Adds each removed element from the stack onto the reversed string
    
    return reversedString

print(reverseStringStack("yeet"))