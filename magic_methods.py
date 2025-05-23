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
    
    # Comparison Operator
    def __eq__(self,other):
        if isinstance(other,InventoryItem):
            return self.name == other.name and self.quantity == other.quantity
        return False
    
    def __lt__(self,other):
        if isinstance(other,InventoryItem) and self.name == other.name:
            return self.quantity < other.quantity
        return ValueError("Cannot compare items of different types.")
    
    def __gt__(self,other):
        if isinstance(other,InventoryItem) and self.name == other.name:
            return self.quantity > other.quantity
        return ValueError("Cannot compare items of different types.")
    


# Create some inventory items
item1 = InventoryItem("Apple", 50)
item2 = InventoryItem("Apple", 30)
item3 = InventoryItem("Banana", 20)

# Adding quantity of the same item
result_add = item1 + item2
print(result_add)

# Subtracting quantity of the same item
result_subtract = item1 - item2
print(result_subtract)

# Multiplying by a factor
result_multiply = item1 * 2
print(result_multiply)

# Comparison between 2
result_compare = item1 == item2
print(result_compare)

# Trying to add items of different types
try:
    result_add_different_types = item1 + item3
except ValueError as e:
    print(e)
