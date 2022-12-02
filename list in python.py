'''list=[]
a=int(input("size" ))
for i in range(0,a):
    v=input("element:" )
    list.append(v)
print("list",list)'''


    
    
'''a=input().split(",")
l=list(a) 
#a=l[::-1]
l.reverse()
print(l)'''


'''a=input("Data1: ")
list1=a.split(",")

b=input("Data2: ")
list2=b.split(",")
if a[0]==b[0] or a[-1]==b[-1]:
    print("True")
else:
    print("False")'''



'''a=input("Data: ")
list1=a.split(",")
size=len(list1)
for i in range(size):
    list1[i]=int(list1[i])
print(list1)
if list1[0]<list1[-1]:
    print("list among:",list1[-1])
else:
    print("list among",list1[0])'''




'''a=input("Data:")
list1=a.split(",")
print("Before updation:",list1)
index=int(input("Index:"))
if index <len(list1) and index>=-(len(list(1))):
                                  value=input("element")
                                  list1[index]=value
                                  print("After updation",list1)
else:
    print("invalid")'''




'''x=(input("X:",))
list1=x.split(",")
print(list1)
y=(input("Y:",))
list2=y.split(",")
print(list2)
print("is equal",list1==list2)
print("is not equal",list1!=list2)'''


data1=input("Data1:")
list1=data1.split(",")
data2=input("Data2:")
list2=data2.split(",")
num=int(input("num"))
print(list1*num)
print(list2*num)
list1.extend(list2)
print("Extending list1 with list2",list1)

 
 
                              
                                 












    
