#Deeya Bachani
#We are going to create a multiplication table For 2
# Using print statement
# input --> user input
# they need to have valid and unique name they will have a unique address
#input--> input ()
print("What is the base?")
base=int(input())
print(type(base))
print("Multiplication table")
print()
print("multiplication of", base)
print()
for var in range (0,11):print(base, "x", var, "=", base*var)
resolved= base*var
