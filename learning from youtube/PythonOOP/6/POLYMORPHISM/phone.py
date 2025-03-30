from item import Item

class Phone (Item):
    # all = [ ]   as we have written super so we also have the acess to the class attributes also 
    def __init__(self, name:str,price:float,quantity:int, broken_phone = 0 ): 
        # call to super function to have acess to all attributes/ method
        super().__init__(name,price,quantity)
        assert broken_phone >=0 ,f"broken phone `{broken_phone}` is not grater than zero!"

        #assign to slef object 
        self.broken_phone = broken_phone