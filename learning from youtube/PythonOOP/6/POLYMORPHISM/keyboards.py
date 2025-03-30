from item import Item

class KeyBoard(Item):
    pay_rate = 0.7
    def __init__(self, name:str,price:float,quantity:int,): 
        # call to super function to have acess to all attributes/ method
        super().__init__(name,price,quantity)