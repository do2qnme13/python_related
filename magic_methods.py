class InventoryItem:

    def __init__(self,name,quantity):
        self.name = name
        self.quantity = quantity
        
    def __repr__(self):
        return f"InventoryItem(name='{self.name}',quantity='{self.quantity}')."

    # Arithmetic Operator
    def __add__(self,other):
        if isinstance(other,InventoryItem) and self.name == other.name:
            return InventoryItem(self.name,self.quantity + other.quantity)
        raise ValueError("Cannot add items of different types.")
    
    def __sub__(self,other):
        if isinstance(other,InventoryItem) and self.name == other.name:
            if self.quantity >= other.quantity:
                return(InventoryItem(self.name,self.quantity - other.quantity))
        raise ValueError("Cannot subtract items of different types.")

    def __mul__(self,factor):
        if isinstance(factor,(int,float)):
            return InventoryItem(self.name,int(self.quantity * factor))
        raise ValueError("Multiplication factor must be a number.")

    def __truediv__(self,factor):
        if isinstance(factor,(int,float)) and factor != 0:
            return InventoryItem(self.name, int(self.quantity / factor)) 
        raise ValueError("Division factor must be a non-zero number.")
    
    