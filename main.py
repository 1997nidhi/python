#!/usr/bin/env python
# coding: utf-8

# In[8]:


def getInput():
        input1=int(input("enter the 1st number to be calculated"))
        input2=int(input("enter the 2nd number to be calculated"))
        return input1,input2
def add():
        x,y=getInput()
        return x+y
def sub():
        x,y=getInput()
        return x-y
        
def mul():
        x,y=getInput()
        return x*y
        
def div():
        x,y=getInput()
        return x//y
def errorHandler():
    return "invalid symbol"
def exit():
    globals()['symbol']=5
    return globals()['symbol']
def main():
        print('''
                 1 for addition
                 2 for subtraction
                 3 for multiplication
                 4 for division
                 5 for exit
                   ''')
        globals()['symbol']=int(input("enter the operation to be done"))
        operations={
            1:add,
            2:sub,
            3:mul,
            4:div,
            5:exit
            }
        output=operations.get(symbol,errorHandler)()
        print(output)
symbol=0       
while symbol!=5:
    main()
print("thankyou")


# In[11]:


from calculator import *
symbol=0
def errorHandler():
    return "invalid symbol"
def exit():
    globals()['symbol']=5
    return globals()['symbol']

def main():
    print('''
             1 for addition
             2 for subtraction
             3 for multiplication
             4 for division
               ''')
    globals()['symbol']=int(input("enter the operation to be done: "))
    operations={
        1:add,
        2:sub,
        3:mul,
        4:div,
        5:exit
        }
    output=operations.get(symbol,errorHandler)()
    print(output)
while symbol!=5:
    main()
print("thankyou")


# In[18]:


from calculation import *
symbol=0
def errorHandler():
    return "invalid symbol"
def exit():
    globals()['symbol']=5
    return globals()['symbol']

def main():
    print('''
             1 for addition
             2 for subtraction
             3 for multiplication
             4 for division
               ''')
    globals()['symbol']=int(input("enter the operation to be done: "))
    operations={
        1:add,
        2:sub,
        3:mul,
        4:div,
        5:exit
        }
    output=operations.get(symbol,errorHandler)()
    print(output)
while symbol!=5:
    main()
print("thankyou")


# In[ ]:




