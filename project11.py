A = int(input("Enter the start of range: "))
B = int(input("Enter the end of range: "))
  

for num in range(A, B + 1):
    if num % 2 == 0:
        print(num, end = " ")
