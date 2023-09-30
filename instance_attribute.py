class Shop:
    shoppingMall="jamuna"
    def __init__(self, buyer):
        self.buyer=buyer
        self.cart=[]

    def add_to_cart(self, item):
        self.cart.append(item)
    
anis= Shop("anis")
anis.add_to_cart("speaker")
anis.add_to_cart("mobile")
print(anis.cart)

minhaj= Shop("minhaj")
minhaj.add_to_cart("glass")
minhaj.add_to_cart("file")
print(minhaj.cart)