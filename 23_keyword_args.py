# keywords arguments = the order of the arguments doesn't matter, unlike positional arguments


def hello(first,lname,age):
    print("hello!"+first,lname,str(age))

#POSITIONAL ARGUMENTS
hello("MOHSIN","CHOUDHARY",33)


#KEYWORDS ARGUMENTS
hello(age=33,first="mohsin",lname="CHOUDHARY")