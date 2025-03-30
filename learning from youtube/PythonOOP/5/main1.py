from item1 import Item
# from phone  import Phone      # using only the parnet  class for under stnading purposes 




Item1 = Item("MY name",750,9)
Item1.name = "other Item"   # changing the name of the instance

print(Item.all)



# but what if we don't want to chnage the name once we have created the instance for that we have make it "read only" i.e we have only one oppurtunity to set the name of the item
# which is know as Encapsulation

item2 = Item("MY name2",750,9) # by creting method  reda_only_name in the item class  which is wraped inside the decorator property

item2.name = "other item 2"

print(item2.name)

# setting new value for read only name   then

item2.read_only_name  = "BB"

# returns 
# Traceback (most recent call last):
#   File "d:\full_stack\MyPractice\Python\learning from youtube\PythonOOP\5\main.py", line 25, in <module>
#     item2.read_only_name  = "BB"
#     ^^^^^^^^^^^^^^^^^^^^
# AttributeError: property 'read_only_name' of 'Item' object has no setter



# no wthe biggest challange is that how to make item2.name as read only 
#which we will do in seprate files 
