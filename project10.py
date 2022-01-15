
ch = input("Enter any character : ")[0]


if ch.isupper() :
    print("\n" + ch, "is UPPERCASE alphabet.")

elif ch.islower() :
    print("\n" + ch, "is LOWERCASE alphabet.")

else :
    print("\n" + ch, "is not an alphabet.")
