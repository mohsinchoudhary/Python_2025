# dictionary comprehension = create dictionaries using an expression
# can replace for loops and certain lambda functions

# dictionary = {key: expression for (key,value) in iterable }
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}

cities_in_f ={'New York':32, 'Boston':75,'Los Angeles':100, 'Chicago':50}

cities_in_C = {key: ((value-32)*(5/9)) for (key,value) in cities_in_f.items()}

print(cities_in_C)

#for key,value in cities_in_C.items():
#    print(key+":"+str(value))


cities_weather ={'New York':"sunny", 'Boston':'winter','Los Angeles':'rainy', 'Chicago':'sunny'}
print(cities_weather)

sunny_city = {key : value  for (key,value) in cities_weather.items() if value == 'sunny'}

print(sunny_city)

city_desc = {key : ('cold' if value<20 else 'warm') for (key,value) in cities_in_C.items()}
print(city_desc)