from item3 import Item


item1 =Item("MyItem",12,10)


print(item1.name)   
# print(item1.__name)   # gives error not able to acess the provate varibale

# now it is only read only attribute

item1.name = "hayyyy"
# now the question that if it is read only so how to change the value of this varibale  , so for that we have some decorators for that

print(item1.name)