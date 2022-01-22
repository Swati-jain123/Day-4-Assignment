# functins 01
def Data():
    a=int(input("enter :"))
    b=float(input("enter :"))
    c=input("enter :")
    d=bool(input("enter :"))
    e=[a,b,c,d]
    f=(a,b,c)
    info={}
    info['name']="lets Upgrade"
    info['class']=5
    g=(info)
    items={1,4,7,95,4,33,89,9}
    print(type(e),type(f),type(g),type(items))
    print(a,b,c,d,e,f,g,items)
    return
Data()
def l():
    lis=[1,67,45,22,98,44]
    for i in enumerate(lis):
        print(i)
l()
def num():
    a=int(input("enter the number : "))
    b=int(input("enter the number : "))
    c=[a,b]
    print(c)
num()

