#All function used in single program
a=[]
def view():
    print(a)
    
    
def insert():
    ch=int(input("1 index \n2 values"))
    if ch==1:
        index=int(input("index:"))
        values=eval(input("values:"))
        a.insert(index,values)
        view()
        
    elif ch==2:
        values=eval(input("values:"))
        a.append(values)
        view()
    else:
        print("Selcet from above:")
#For delete
def delete():
    ch=int(input("1 index \n2 element"))
    if ch==1:
        index=int(input("index:"))
        a.pop(index)
        view()
        
    elif ch==2:
        element=eval(input("element:"))
        a.remove(element)
        view()
        
#for replace

def replace():
    oldvalue=eval(input("Oldvalue:"))
    Newvalue=eval(input("Newvalue:"))
    a.replace(oldvalue,Newvalue)
    view()
    
while True:
    print("1 view \n2 insert \n3 delete \n4 replace \n5 Exists")
    ch=int(input("Choice:"))
    if ch==1:
        view()
    elif ch==2:
        insert()
        
    elif ch==3:
        delete()
        
    else:
        break
    
       
        