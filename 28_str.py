# str.format

animal = "cow"
item = "moon"

print("the {} jumped over the {}".format(item,animal))

print("the {1} jumped over the {0}".format(item,animal))#positional argument

print("the {animal} jumped over the {item}".format(item="moon",animal="cat"))#keyword argument

text = "the {} jumped over the {}"

print(text.format(animal,item))