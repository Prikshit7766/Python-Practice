# multiple classes inheritance
class Bank:
    def transection(self):
        print("total transection value")
    def account_opening(self):
        print("this will show you your account open status")

    def deposite(self):
        print("this will show your deposite amount")
    def test(self):
        print("this is a test method from Bank class")


class HDFC_bank:
    def  hdf_to_icici(self):
        print("this will show all the transection happend to icici to hdfc")

    def test(self):
        print("this is a test method from HDFC_Bank class")

class ineuron_bank:
    def account_stratus_icici(self):
        print("print ACCOUNT status in icici")
class icici(Bank,HDFC_bank,ineuron_bank):
    pass

i=icici()
i.deposite()
i.hdf_to_icici()
i.account_opening()
i.transection()
i.test() # it is going to execute test method from bank class as  bank class is written first  in ()
# if there is is a conflict w.r.t to name  then by defaut it is going to give priority to class which is written first

# still we are able to inherite all the properties from both the classes


i.account_stratus_icici()