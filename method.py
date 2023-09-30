def call():
    print("i call someone")
    return "call done"


class Phone:
    price= 25000
    brand= "samsung"
    features=["camera", "hammer"]

    def call(self):
        print("call one person")
    def send_sms(self, phone, sms):
        text= f"phone is {phone} and sms is {sms}"
        return text

my_phone= Phone()
# print(my_phone.brand)
# print(my_phone.call())
res= my_phone.send_sms(4152,"anis learning")
print(res)