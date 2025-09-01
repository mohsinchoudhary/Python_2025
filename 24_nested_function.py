#calling a function inside another function is nested function


num = input("Enter a number:")

num=float(num)
num=abs(num)


print(num)

#or 
print(abs(float(input("Enter a number:"))))