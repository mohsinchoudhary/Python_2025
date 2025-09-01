# sort() method = used with lists
# sorted() function = used with iterables


students = ["Mohsin","Choudhary","Ayman","Rayyan"]



students.sort(reverse=True) #sorts the list permanently
print(students)


students_tup = ("Mohsin","Choudhary","Ayman","Rayyan")
sorted_student = sorted(students_tup,reverse=True) #sorts the tuples 
print(sorted_student)

collg_student = [("Mohsin","B",60),
                  ("Choudhary","C",55),
                  ("Ayman","A",14),
                  ("Rayyan","A",10)
                  ]
#sort by age
grades = lambda grades:grades[2]
#print(collg_student[grades])
collg_student.sort(key=grades)

for i in collg_student:
    print(i)