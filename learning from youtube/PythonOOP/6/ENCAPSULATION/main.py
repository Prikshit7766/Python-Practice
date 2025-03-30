#encapsulation is  restricting the ability to over write the values of your object within your ``setter``
#encapsulation  not allow to change the value of the object directly
from item import Item


item=Item("my item",700)
item.apply_increment(0.2)  # now we are able to change the price  
# but
# item.price = 1000  #this is will  give error
print(Item.all)