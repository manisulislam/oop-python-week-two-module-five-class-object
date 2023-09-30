# def call():
#     print('calling someone i dont know')
#     return 'call done'


# class Phone:
#     price = 12000
#     color = 'blue'
#     brand = 'samsung'
#     features = ['camera', 'speaker', 'hammer']


#     def call(self):
#         print('calling someone i know')



# my_phone = Phone()
# call()
class Phone:
    price = 12000
    color = 'blue'
    brand = 'samsung'

    def call(self):
        print('calling one person')

    def send_sms(self, phone, sms):
        text = f'Sending SMS to: {phone+5}'
        return text


my_phone = Phone()
result = my_phone.send_sms(41524, 'Missy, I missed to miss you')
print(result)