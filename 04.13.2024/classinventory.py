class Inventory:
    def __init__ (self,item_id,item_name,stock_count,price):
        self.item_id = item_id
        self.item_name = item_name
        self.stock_count = stock_count
        self.price=price
    def add_item(self):
        item_details={
            self.item_id: {
                "Item Name": self.item_name,
                "Stock Count": self.stock_count,
                "Price": self.price
            }
        }
        return item_details
        

item1 = Inventory(100,"Laptop",100,200000)
item2 = Inventory(102,"Kaye",100,200000)

print(item1.add_item())
print(item2.add_item())