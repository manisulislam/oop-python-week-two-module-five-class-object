class Shop:
    cart=[]
    def __init__(self, buyer):
        self.buyer=buyer
    def add_to_cart(self, item):
        self.cart.append(item)
anis= Shop("anis")
anis.add_to_cart("bag")
anis.add_to_cart("laptop")
anis.add_to_cart("book")
print(anis.cart)

afrin= Shop("afrin")
afrin.add_to_cart("watch")
afrin.add_to_cart("pen")

print(afrin.cart)