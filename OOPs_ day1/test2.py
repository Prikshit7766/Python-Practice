class Person : # created the Person class
    def __init__(a,name,sur_name,email_id,year_of_birth): # __int__ is default inbuild method which will be avilabe
        # chnaging self to a ,it is just a reference i.e pointer
        a.name1 = name
        a.sur_name=sur_name
        a.email_id=email_id
        a.year_of_birth = year_of_birth

    def age(a,curr_year):
        return(curr_year-a.year_of_birth)


anuj_var=Person("anuj","bhandari","anuj@gmail.com",1944) # here we have decleared one variable and one by one we are passing data, but how it is waorking?
sudh=Person("sudhanshu","kumar","sudhanshu#gmail,com",1987)
gargi=Person("gargi","kumar","sudhanshu@gmail.com",2122)
print(anuj_var.name1)
print(anuj_var.sur_name)
print(anuj_var.email_id)
print(anuj_var.year_of_birth)
print(sudh.name1)
print(sudh.sur_name)
print(sudh.email_id)
print(sudh.year_of_birth)

print(type(sudh.name1))

# can you give me concatation of name and sur_name for sudhanshu
z=(sudh.name1)+(sudh.sur_name)

print(z)

print(sudh.age(2022))
s="sudh"
s.upper()