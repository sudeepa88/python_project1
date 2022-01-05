list1=[]
list3=[]
list5=0
temp=0

n=int(input("Enter numbers of integers: "))
print("Enter integers: ")
for i in range(0,n):
    x=input()
    list1.append(x)
print("Here is the list: ")
print(list1)
list2=tuple(list1)
print("Here is the Tuple: ")
print(list2)
list4=len(list1)

for i in range(0,list4):
    temp= temp + int(list1[i])
list3.append(temp)
list5=(int(list3[0]))/n

    
print("Here is the value of average of all elements in tuple is: ",list5)
    
