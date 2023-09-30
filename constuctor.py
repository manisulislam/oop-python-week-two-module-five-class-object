
class Phone:
    taka= 25000
    name= "samsung"
    features=["camera", "hammer"]

    def __init__(self, owner,brand, price):
        self.owner=owner
        self.brand=brand
        self.price=price


    def send_sms(self, phone, sms):
        text= f"phone is {phone} and sms is {sms}"
        return text

my_phone= Phone("anis", "itel", 6520)
# print(my_phone.brand)
# print(my_phone.call())
res= my_phone.send_sms(4152,"anis learning")
print(res)

print(my_phone.owner,my_phone.brand, my_phone.price)