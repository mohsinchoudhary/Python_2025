# filter = create a collection of elements from an iterable for which a function returns true
# filter (function,iterable)


Friends = [ ( "Rachel",19),
           ( "Monica",18),
           ( "Phoebe",21),
           ( "Ross",10),
           ( "Chandler",14),
           ( "Joey",19)
           ]

#lambda data : Friends[0][1] >
age = lambda data : data[1] > 18
print(list(filter (age,Friends)))