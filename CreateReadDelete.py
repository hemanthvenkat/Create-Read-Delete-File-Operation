
#This is CURD function operations
import threading 
from threading import*
import time

dic={}

def Read(key):
    if key not in dic:
        print("error: enter a valid key ") 
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri
        

def Create(key,value,timelimit=0):
    if key in dic:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timelimit==0:
                    l=[value,timelimit]
                else:
                    l=[value,time.time()+timelimit]
                if len(key)<=32: 
                    dic[key]=l
            else:
                print("error: Memory limit exceeded ")
        else:
            print("error: Invalind key_name, it should contain only alphabets and no special characters or numbers")


def Delete(key):
    if key not in dic:
        print("error: enter a valid key") 
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del dic[key]
                print("key is deleted")
            else:
                print("error:",key,"time to live has expired")
        else:
            del dic[key]
            print("key is  deleted")



def modify(key,value):
    b=dic[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dic:
                print("error: enter a valid key") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dic[key]=l
        else:
            print("error:",key," time-to-live has expired ") 
    else:
        if key not in dic:
            print("error: enter a valid key ") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dic[key]=l


Create("Amrita",69)


Create("freshworks",70,3600)

Read("Amrita")

Read("freshworks")

Create("Amrita",50)

Modify("Amrita",55)

Delete("Amrita")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()
