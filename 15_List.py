# list = used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti"]
#each item is an element
#print(food)

#access using indexm first position, this will print pizza
#print(food[0])

#we can always update and change elements
food[0] = "sushi"
#print(food[0])


#print all elements in index using a loop
#for x in food:
#    print(x)


#functions of list 
food.append("ice cream")
food.remove("hotdog")
food.pop()#this will remove last element i.e ice cream
food.insert(0,"cake")#this will add code at index 0, shushi will move to index 1
food.sort()
food.clear()#clear the list
for x in food:
    print(x)
