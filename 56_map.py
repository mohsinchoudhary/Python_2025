# map = applies a function to each item in an iterable(list,tuple ets)
# map(function,iterable)

store = [("shirt",40.00),
         ("pants",55.00),
         ("jacket",100.00),
         ("socks",10.00)]

to_euros = lambda data : (data[0],data[1]*0.88)

to_dollars = lambda data : (data[0],data[1]/0.88)

store_euros = list(map(to_euros,store))

store_dollar = list(map(to_dollars,store))

for i in to_euros:
    print(i)