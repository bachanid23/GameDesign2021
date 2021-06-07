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
print("What is the base?")
base=int(input())
print(type(base))
print("addition table")
print()
print("addition of", base)
print()
for var in range (0,11):print(base, "+", var, "=", base+var)
resolved= base+var
print("What is the base?")
base=int(input())
print(type(base))
print("subtraction table")
print()
print("subtraction of", base)
print()
for var in range (0,11):print(base, "-", var, "=", base-var)
resolved= base-var
print("What is the base?")
base=int(input())
print(type(base))
print("division table")
print()
print("division of", base)
print()
for var in range (1,11):print(base, "/", var, "=", base%var)
resolved= base%var
