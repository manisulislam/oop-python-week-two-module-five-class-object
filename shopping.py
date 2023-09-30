class Shop:
    def __init__(self, name):
        self.name= name
        self.cart= []
    def add_to_cart(self, item, price, quantity):
        product={"item": item, "price": price, "quantity": quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total= 0
        for item in self.cart:
            # print(item)
            total+=item["price"]* item["quantity"]
            
            if amount <total:
                print(f"aro {total-amount} taka lagbe")
            else:
                print(f"tomar taka {amount-total} nao")
            
        print(total)
anis= Shop("anis")
anis.add_to_cart("rice", 50, 3)
anis.add_to_cart("dim", 100, 12)
anis.add_to_cart("fish",250,3)
print(anis.cart)

anis.checkout(500)