# here we are going to write __init__    which one it is going to consider
class Person : # created the Person class
    def __init__(a,name,sur_name,email_id,year_of_birth):

        a.name1 = name
        a.sur_name=sur_name
        a.email_id=email_id
        a.year_of_birth = year_of_birth
    def __init__(a,name,sur_name ):
        a.name1 = name
        a.sur_name=sur_name
# gives you error
    def age(a,curr_year):
        return(curr_year)
# also it is considering the second init and overwriting the first one


anuj_var=Person("anuj","bhandari")
sudh=Person("sudhanshu","kumar")
gargi=Person("gargi","kumar")


print(sudh.age(2022))
s="sudh"
s.upper()

