from matplotlib import pyplot as p
import mpmath as mp
from sympy import *
x=symbols('x')
from math import *
m=[]
l=[]
m2=[]
l2=[]
rnn=[]
rnm=[]
def bisec(q,a,b,n):
    for i in range(n):
        x=a
        f=eval(q)
        x=b
        f2=eval(q)
        x=(a+b)/2
        f1=eval(q)
        if(f*f1<0):
            f1=eval(q)
            d=(a+b)/2
            m.append(i)
            l.append(d)
            print(i+1,"->",a,"=",b,"=",d,"=",f1)
            b=x
        elif(f*f1>0):
            #x=(a+b)/2
            f1=eval(q)
            d=mp.mpf((a+b)/2)
            m.append(i)
            l.append(d)
            print(i+1,"->",a,"=",b,"=",d,"=",f1)
            a=x
        else:
            d=mp.mpf((a+b)/2)
            m.append(i)
            l.append(d)
            print(i+1,"->",a,"=",b,"=",d,"=",f1)
def rf(q,a,b,n):
    px=0
    for i in range(n):
            x=a
            y=eval(q)
            x=b
            y2=eval(q)
            xn=(((a-b)*y)/(y2-y))+a
            k=((xn-px)/xn)*100
            x=xn
            f=eval(q)
            m2.append(i)
            l2.append(x)
            if(y*f<0):
                b=xn
                xn=(((a-b)*y)/(y2-y))+a
                print(i+1,"->",round(a,5),"=",round(b,5),"=",round(y,5),"=",round(y2,5),"=",round(xn,5),"=",round(f,5),"=",round(abs(k),5))
                px=xn
            elif(y*f>0):
                a=xn
                xn=(((a-b)*y)/(y2-y))+a
                print(i+1,"->",round(a,5),"=",round(b,5),"=",round(y,5),"=",round(y2,5),"=",round(xn,5),"=",round(f,5),"=",round(abs(k),5))
                px=xn    
            else:
                print("root already found")
                
def rn(q,z,aaaa,n):
    aaaa=str(aaaa)
    x=z
    for i in range(n):
        x0=x-(eval(q)/eval(aaaa))#(f/f2)
        rnn.append(i)
        rnm.append(x)
        print(i+1,"-",x0)
        x=x0
def intv(z,q):
    x=z
    while True:
        a=x
        x=a
        fi=eval(q)
        x=x+1
        b=x
        x=b
        fr=eval(q)
        if(fi*fr<0):
            break
        return(a,b)
def comg():
    
    while True:
        
        q=input("enter the expression:-")
        #zz=float(input("enter the initial value for interval:-"))
        #a,b=intv(z,q)
        z=float(input("enter the inital value for RN method:-"))
        aaaa=diff(q,x)
        a=float(input("enter the a value:-"))
        b=float(input("enter the a value:-"))
        print("rf:-\n")
        rf(q,a,b,n)
        print("bisec:-\n")
        bisec(q,a,b,n)
        print("nr:-\n")
        rn(q,z,aaaa,n)
        p.plot(rnn,rnm,"g-",label="NEWTON RAPSON")  
        p.plot(m,l,"r-",label="BISECTION")  
        p.plot(m2,l2,"b--",label="REGULAR FALSE")
        p.legend()
        p.title("f(x)="+q)
        p.xlabel("X-axis=no of iterations")
        p.ylabel("Y-axis=x values")
        p.show()
comg()
