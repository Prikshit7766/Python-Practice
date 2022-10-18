class person1:
    def __init__(self,name,surname,year):
        self._name1=name  # by writing _ befor the variable then it will become protected
        self.__surname1 = surname # __ private
        self.year1 = year
        #by defalut all the will be public

sudh = person1("sudhanshu","kumar",1990)
print(sudh._name1)
#print(sudh.__surname1) # not working but i am calling  but why

# There are three types of access modifiers in Python: public, private, and protected.
# Variables with the public access modifiers can be accessed anywhere inside or outside the class,
# the private variables can only be accessed inside the class, while protected variables can be accessed within the same package.

print(sudh._person1__surname1) # this is the  way of acessing protected varible
