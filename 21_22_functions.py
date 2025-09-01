# functions is a block of code which only runs when it is called



def hello(name,lname,age):
    print("hello! "+name," "+lname)
    print("your age "+str(age))
    print("have a nice day")

my_name,surname = "Mohsin","Choudhary"
hello(my_name,surname,21)#bro is argument here


def multiply(number1,number2):
    return number1*number2


print(multiply(2,5))