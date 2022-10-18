class person1:
    def __init__(self,name,surname,year):
        self._name1=name
        self.__surname1 = surname
        self.year1 = year


sudh = person1("sudhanshu","kumar",1990)
print(sudh._name1)
print(sudh._person1__surname1) # this is the  way of acessing protected varible
