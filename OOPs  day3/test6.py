# encaptulation

class ineuron:
    def __init__(self):
        self.students1="data science"
    def students(self):
        print(self.students1)
  # conflict ---> method name and variable name should not be same




i=ineuron()

i.students()

i.students1="data analytics"

i.students()


# printing data analytics  i.e it is overwriting


class ineuron1:
    def __init__(self):
        self.__students1="data science"
    def students(self):
        print(self.__students1)
 # i am able to acces the private variable

    def student_change(self,new_value):
        self.__students1 = new_value

i1=ineuron1()

i1.students()

i1.__student1 ="big data"
i1.students()

# here we  apling the same operation w.r.t  private variable
# this time it has not overwritten the value
# no it has not chnaged


i1.student_change("Prikshit")
i1.students()
 # now it is changing the private variable
 # here we are chnaging the value inside a class by calling some other method and inside that method we are trying to seclar new values

# this phenomenon is called as encaptulation
# concept of encaptulation says that  you are not suppose to allow the user to modily the value of the varibale directly  then you will be albe to achive capsule so that no one able to change it directly