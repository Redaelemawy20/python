class PaymentService: 
    trans_number = 0
    def __init__(self, fees=0):
        print('init payment services')
        self.fees = fees

    def pay_money(self, account_balance, amount):
        print('excute payment with {} fees'.format(self.fees))
        print('balance = {} - {} - {} = {}'.format(account_balance, amount, self.fees, account_balance - amount - self.fees))
        PaymentService.trans_number += 1
    @classmethod
    def get_trans_number(cls):
        print('number of transactions is {}'.format(cls.trans_number))


class StripPaymentService(PaymentService):
    def pay_money(self, account_balance, amount):
        print('pay with stripe')
        super().pay_money(account_balance, amount)

class PaypalPaymentService(PaymentService):
    def pay_money(self, account_balance, amount):
        print('pay with paypal')
        super().pay_money(account_balance, amount)


PaymentService.trans_number = 383892;   
py = PaymentService()
print(py.trans_number)     
# py.pay_money(100, 5)

strip = StripPaymentService(1)
# strip.pay_money(100, 5)
strip.trans_number = 20000
print(py.trans_number) 
(py.get_trans_number())
print(strip.trans_number)
(strip.get_trans_number())
PaymentService.trans_number =543253;    
print(py.trans_number) 
(py.get_trans_number())
print(strip.trans_number)    
(strip.get_trans_number())



paypal = PaypalPaymentService(.5)
# paypal.pay_money(100, 5)

PaymentService.get_trans_number()
# strip.get_trans_number()