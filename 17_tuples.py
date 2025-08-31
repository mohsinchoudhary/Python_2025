# tuple = similar to list but its ordered and cannot be changed
# useful for grouping related data
# use set of parenthesis instead of square bracket
student =  ("Bro",21,"male")

#use functions, there are only 2 functions
print(student.count("Bro"))
#find index
print(student.index("male"))

#iterate over tuples
for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here")