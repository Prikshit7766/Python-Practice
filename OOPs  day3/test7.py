#polymorpsim
class ineuron:
    def students(self):
        print("print  a student details ")

class class_type:
    def students(self):
        print("print the class type of student")

def ineuron_external(a):
    a.students()


i=ineuron()
j=class_type()
ineuron_external(i)
ineuron_external(j)
# here we are using the same function but it is  calling the method of different class  based on what we are passing i.e data
# one function is bale to handle i and j ... function is same  but bheviour is chnaging
# we can say that this function is like a commen interface



def test(a,b):
    return a+b
print(test(3,4)) # passing int --> doing addition
print(test("sudhanshu" , " kumar")) # passing str --->  doning concatation
# function is same , argument is also same   but its behavour has change when we have chnaged the data
# one objct --> different behaviour   --> this phenomenon is called as #polymorpsim
