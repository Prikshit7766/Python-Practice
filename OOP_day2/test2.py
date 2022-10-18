class person: #it is called as parent class
    _name="sudh"
    __surname="kumar"
    yob =1990
    # here we not using __init__ method
    # here we are creating simple varibale
    # and i am not suppose to pass this data at all

    def _age(self,curr_year):
        return curr_year - self.yob
    def __age1(self,curr_year):
        return curr_year - self.yob
obj=person()
print(obj)
print(obj._age(2022)) # calling the protected function
print(obj._person__age1(2022)) # calling private function

class employee(person): # here we are expecting properties of person class in emplyee class
     # employee class will be called as child class
     _name="Prikshit" # name is modifided
     __surname = "singh" # surname is not changed
     yob =1991  # year is also changed

obj1=employee()
print(obj1._age(2022)) # as we have updated the year of birth
print(obj1._person__age1(2022))
print(obj1)
print(obj1.yob) # it is inheriting the properties from person class inside the employee class

print(obj1._name)
print(obj1._person__surname)
print(obj1._employee__surname)
 # are overwriting protected and public variable


