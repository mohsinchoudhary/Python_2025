# set = collection which is unordered , unidexed. No duplicate values
# use {}
# set is faster than list for searching
utensils = {"fork","spoon","knife","knife","knife"}

dishes = {"bowl","plate","cup","knife"}

#add an element
utensils.add("napkin")
#remove
utensils.remove("fork")
#clear
#utensils.clear()
# unordered - everytim we run for loop the sequence of output will be different as its not ordered
for x in utensils:
    #print(x)
    x


#this will merge two sets
utensils.update(dishes)
for x in utensils:
    #print(x)
    x

#we can also join
dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

# we can also find common(intersection) and difference(difference)
print(utensils.difference(dishes))