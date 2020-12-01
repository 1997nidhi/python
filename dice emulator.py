#!/usr/bin/env python
# coding: utf-8

# In[5]:


from random import *
def rolling(x):
    while x=="y":
        num=randint(1,6)
        if num==1:
            print("|       |")
            print("|   *   |")
            print("|       |")
        if num==2:
            print("| *     |")
            print("|       |")
            print("|     * |")
        if num==3:
            print("| *     |")
            print("|   *   |")
            print("|     * |")
        if num==4:
            print("| *   * |")
            print("|       |")
            print("| *   * |")
        if num==5:
            print("| *    * |")
            print("|    *   |")
            print("| *    * |")
        if num==6:
            print("| *   * |")
            print("| *   * |")
            print("| *   * |")
        x=input("enter 'y' to continue the game or 'n' to exit")
        print("\n")
x="y"
rolling(x)





