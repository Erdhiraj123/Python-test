#Decorator in Python

def decorator(call):
    def abc():
        print("befor abc calling")
        call()
        print("after calling ")
    return abc
    
    
@decorator
def fun():
    print("hello bro")
    print("would you like to take some food")
    
fun()