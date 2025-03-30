# overwriting
class ineuron:
    def student(self):
        print("print all the detail of the student")
    def achiver(self):
        print("print the list of all the achiver")

    def hall_of_fame(self):
        print("print everyone from hall of fame")


class ineuron_vision(ineuron):
    def student(self):
        print("these are the filtered student list")


iv=ineuron_vision()
iv.student() # overwrite the student method and execute the student method from ineuron_vision
 # this is called as method overwriting



