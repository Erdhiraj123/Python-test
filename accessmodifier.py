#Access Modifier in Encapsulation in python

#Private modifier 
class A:
    def __abc(self,x,y):
        self.x=x
        self.y=y
        print("sum of two number is:",self.x+self.y)
    def call(self):
        print("calling private modifier")
        obj=A()
        obj.__abc(13,19)
        
obj1=A()
obj1.call()             #Output
                        #calling private modifier
                        #sum of two number is: 32


#Protective modifier
class B:
    def _abc(self,a,b):
        self.a=a
        self.b=b
        print("substraion of two number is:",self.a-self.b)
     
class C(B):
    def fun(self):
        print("calling protective modifier in inheritated class")
        obj=B()
        obj._abc(19,10)
        
obj1=C()
obj1.fun()              #Output
                        #calling protective modifier in inheritated class
                        #substraion of two number is: 9
                         

#Public modifier
class C:
    def fun(self,x,y):
        self.x=x
        self.y=y
        print("calling public modifer")
        print("multiplication of two number is:",self.x*self.y)
            
obj1=C()
obj1.fun(12,2)          #Output
                        #calling public modifer
                        #multiplication of two number is: 24
