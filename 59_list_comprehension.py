# list comprehension = a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [a.expression b.for item c.in d.iterable ifcondition == True]
# list = [a.expression b.if/else c.for item d.in e.iterable]


squares = []

for i in range(1,11):
    squares.append(i*i)

print(squares)

#list comprehension
squares = [i*i for i in range(1,11)]
print(squares)

student = [100,50,60,88,45,10,95]

passed_student = [i for i in student if i >=50]

passed_student = [ i if i >=50 else "Failed" for i in student ]


print(passed_student)

#using lambda annd filter
print(list(filter(lambda x : x>= 50, student)))



