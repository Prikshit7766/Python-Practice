# multilable inheritance
class Bank:
    def transection(self):
        print("total transection value")
    def account_opening(self):
        print("this will show you your account open status")

    def deposite(self):
        print("this will show your deposite amount")


class HDFC_bank(Bank): # child class of bank
    def  hdf_to_icici(self):
        print("this will show all the transection happend to icici to hdfc")

class icici(HDFC_bank): # by calling HDFC_bank by default all the functionin the hdfc_bank will be avilable
                        # and hdfc_bank any how calling the Bank class
                        # so both the classes Bnak and HDFC_bank will be available
    pass

i=icici()
i.hdf_to_icici()
i.transection()
i.account_opening()
i.deposite()
# all the four methods are avilabe for the icici class

