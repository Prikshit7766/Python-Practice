class Person : # created the Person class
    def __init__(self,name,sur_name,email_id,year_of_birth): # __int__ is default inbuild method which will be avilabe
        # self is not a varible , it is just a reference i.e pointer
        # use of the __init__ is pass the data to my classes , so that it can give me some kind of return
        # these are the  commen things which the person have
        self.name=name # self.name ---> is class variable   and   self.name  and name are not same
        self.sur_name=sur_name
        self.email_id=email_id
        self.year_of_birth = year_of_birth


anuj_var=Person("anuj","bhandari","anuj@gmail.com",1944) # here we have decleared one variable and one by one we are passing data, but how it is waorking?
sudh=Person("sudhanshu","kumar","sudhanshu#gmail,com",121212)
gargi=Person("gargi","kumar","sudhanshu@gmail.com",2122)
print(anuj_var.name)
print(anuj_var.sur_name)
print(anuj_var.email_id)
print(anuj_var.year_of_birth)
print(sudh.name)
print(sudh.sur_name)
print(sudh.email_id)
print(sudh.year_of_birth)

print(type(sudh))

