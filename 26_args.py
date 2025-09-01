#*args = parameter that will pack all the arguments into a tuple
# useful so that a function can accept a varying amount of arguments


#def addition(num1,num2):
def addition(*stuff):#packing all the arguments into a tuple,args
    #return num1+num2
    #stuff[0]=10, this will not work as we cannot change tuples
    #stuff=list(stuff) this will work as tuple is converted to list
    #stuff[0]=10,
    sum=0
    for i in stuff:
        sum += i
    return sum

print(addition(1,2,3))