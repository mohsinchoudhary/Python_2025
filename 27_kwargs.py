#kwargs = parameter that will pack all the arguments into a dictionary
#useful so that a function can accept a varying amount of keyword arguments

#this will give error as middle in not present in function definition
#def hello(first,lname):
#    print("hello!"+first,lname)
def hello(**kwargs):
    print("Hello "+kwargs['first']+" "+kwargs['lname'],end=" ")
    for key,value in kwargs.items():
        print(key+" "+value,end=" ")


hello(first="Mohsin",lname="choudhary",middle=" ")

