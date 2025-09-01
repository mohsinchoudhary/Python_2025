# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets etc.)

#list
user_name = ['Mohsn','Vasim']
#tuple
password = ('abc123','xyz123')

users = dict(zip(user_name,password))
print(type(users))
#for i in users:
#    print(i)

for key,value in users.items():
    print(key+":"+value)