tupleObj=(12,34,19,45,22,33,19)
print(tupleObj)
tuple3=list(tupleObj)
tuple3[2]=67
tupleObj=tuple(tuple3)

print(tupleObj)
print("19 replaced by 67.")
