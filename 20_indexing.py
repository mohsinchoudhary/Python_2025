# index operator[] = gives access to a sequence's element(str,list,tuples)

name = "bro Code!"

#use [] and integer to access and element in string
if (name[0].islower()):
    name = name.capitalize()
print(name)

# [0:3] or [:3] if index start at 0
first_name = name[:3].upper()
last_name = name[4:].upper().lower()

#negative will print last element
last_character = name[-1]
print(first_name)

print(last_name)
print(last_character)