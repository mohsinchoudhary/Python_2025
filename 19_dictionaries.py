# dictionary = Changeable,unordered key value pair of unique key:value pairs
# its fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC', 
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'
            }

#instead of using number index we need to use key (as dictionary is unordered)
print(capitals['Russia'])

#print error is its not present
#print(capitals['Germany'])

#get method is useful as it will not throw error if key is not present
print(capitals.get('Russia'))
print(capitals.get('Germany'))


# print only keys
print(capitals.keys())

# print only values
print(capitals.values())

# print both key and valyes
#print(capitals.items())


#for key,value in capitals.items():
#    print(key,":",value)

#key can be changed, use update method for adding new and updating existing key value

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'New York'})
for key,value in capitals.items():
    print(key,":",value)

#remove a key value pair
capitals.pop('China')
# capitals.clear() will remove everything

"""1. Finding the Maximum Value Directly:
To get only the maximum value from the dictionary's values, use max() on the values() view:"""

my_dict = {'apple': 10, 'banana': 25, 'cherry': 15}
max_value = max(my_dict.values())
print(max_value)


"""2. Finding the Key Associated with the Maximum Value:
To find the key corresponding to the maximum value, use max() with the key argument set to dict.get:"""

my_dict = {'apple': 10, 'banana': 25, 'cherry': 15}
max_key = max(my_dict, key=my_dict.get)
print(max_key)