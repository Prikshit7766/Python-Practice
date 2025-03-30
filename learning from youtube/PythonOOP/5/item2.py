import  csv

class Item:
    pay_rate = 0.8  
    all = []
    def __init__(self, name:str,price:float,quantity:int): 
        # run validation 
        assert price >=0,f"price `{price}` is not grater than zero!"
        assert quantity >=0 ,f"quantity `{quantity}` is not grater than zero!"
        #assign to self object 
        self._name = name   # we will add _ befor the varibale name  becuse method name and varibale are there at the ame time which is creating the problem 
        self.price =price
        self.quantity = quantity
        
        # Action to exectue
        Item.all.append(self)  

    @property
    #Peopertry  Decorator  =  Read-Only Attrbute
    def name(self):
        #some action or condition
        return self._name 


    def calcilate_total_price(self):
        return self.price * self.quantity

    
    def apply_discount(self,):
        self.price =self.price * self.pay_rate     
        return self.price 

    @classmethod   
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader =  csv.DictReader(f) # this will read the csv as list of dictionary
            items = list(reader)   # converting reader into list


        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity=  int(item.get('quantity')),
            )

    @staticmethod           # this means that this static method never sending in background the instance as first argument 
    def is_interger(num):   # stand alone or isolated function
        # we wll count out the float that are point zero

        #for i.e: 5.0, 10.0
        if isinstance(num, float):

            # count out the float that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else : 
            return False

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r},{self.price!r},{self.quantity!r})"
    



    