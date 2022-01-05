tuple1 = (7,8,9,10)
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
tuple4 = list(tuple3)


tuple_length= len(tuple4)

for i in range(0,tuple_length-1):
    for j in range(i+1,tuple_length):
        if(tuple4[i]>tuple4[j]):
          temp=tuple4[i]
          tuple4[i]=tuple4[j]
          tuple4[j]= temp
     
    
        
tuple5= tuple(tuple4)
print(tuple5)             
