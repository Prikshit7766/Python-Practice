class car: # parent class
    def __init__(self,body,engin,tyre):
        self.body=body
        self.engine=engin
        self.tyre=tyre

    def milage(self):
        print("milage of the class")


#child class
class tata(car): # inheriteance operation  , here you have to behave in the similar way as parent class otherwise it will give error
    pass


c=car("solid","v6","radial")
print(c)

#t=tata()
#print(t) ---> gives you error as we have not passed there parameters
# so we have to do like

t=tata("solid","v8","radial")

print(t)

print(t.tyre)
print(t.milage())
