class person :
    def age(self,curr_year,yesr_of_birth):
        return curr_year- yesr_of_birth
    def email_id_input(self,email_id):
        print("take and mail if from a person  and print it" ,email_id)
    def ask_name(self):
        name=input("tell e your name")
        return name
    def as_date_of_birth(self):
        dob=input("tell me your date of birth")
        return dob
# here we have not created the constructer  and the role of the constructor is to  take a input from the user
sudh=person()
anuj=person()
gargi=person()
hitash=person()
prikshit=person()

sudh.email_id_input("sudhi12i@gmail.com")
print(sudh.ask_name())

print(hitash.as_date_of_birth())


# now it became a generic function
# now we can increase the saclibility of the code
# reusablity of code
# very structured and to maintain the code
# not scattered

"""Task 1 - in a past whatever questions i have given to your with respect to list ,
tuple , dic , set , string try to create a seprate class for each and everyting and
    restructure your code for all the segment and submit .

instruction number 1 -
    always use exception handling
instrruction number 2 :
    use loggging as well

Reformat your code and submit it to me before tomorrwo's' class 3 PM IST to my mail id
sudhanshu@ineuron.ai
sunny.savita@ineuron.ai
