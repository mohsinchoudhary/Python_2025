# reduce() = apply a function to an iterable and reduce it to a single cumulative value
# perform function on first two elements and repeat process until 1 value remains

# reduce (function,iterable)

from functools import reduce

letter = ["H","E","L","L","O"]

word = reduce( lambda x,y: x+y, letter)
print(word)



factorial = [5,4,3,2,1]

word = reduce( lambda x,y:x*y , factorial)
print(word)