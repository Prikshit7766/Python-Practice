from item2 import Item


item1 =Item("MyItem",12,10)


print(item1.name) 

# item1.name = "new name"  # give error now it is read only


# print(item1.name)


# but 

item1._name = "new name"  # this varible is protected varibale,but we can also change the name in this way but to avoid this we can add one more  _  and make it like  self.__name   to make it private varibale 


print(item1.name)