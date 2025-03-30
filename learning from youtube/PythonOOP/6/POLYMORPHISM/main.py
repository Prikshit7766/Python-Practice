from phone import Phone
from keyboards import KeyBoard


item1  = Phone ("js",1000,2)

item1.apply_discount()
print(item1.price)



item2= KeyBoard("js Keyboard",1220,21)

item2.apply_discount()

print(item2.price)