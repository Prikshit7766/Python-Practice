# Destructors!
# decstructor is called when your object is no loger is needed or out of scope
# who calls it ?
# python garbage collector which keep track of all the objects and destroy them if they are no longer referenced

class Destruct :
    n_objects = 0   # class variable

    def __init__(self) -> None:
        Destruct.n_objects += 1   # here we are not using self because Destruct is a class level variable

    @classmethod
    def numberofobject(cls):
        print("Number of objects created till now : ", cls.n_objects)

    def __del__(self):
        Destruct.n_objects -= 1
        print("Object destroyed")

    
def outofscopetest():
    destruct = Destruct()
    destruct.numberofobject()


if __name__ == "__main__":
    destruct = Destruct()
    destruct.numberofobject()
    print("calling outofscopetest()")
    outofscopetest()
    print("outofscopetest()  is completed")
    destruct.numberofobject()
    print("End of main")



    # output
# Number of objects created till now :  1
# calling outofscopetest()
# Number of objects created till now :  2
# Object destroyed
# outofscopetest()  is completed
# Number of objects created till now :  1
# End of main