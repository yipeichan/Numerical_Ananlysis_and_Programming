class cash(object):
    'An example class to handle cash in different currency'

    def __init__(self, amount = 0., currency = 'TWD'):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return str(self.amount)+' '+self.currency

    def convert(self, target_currency = 'EUR'):
    # converting from self.currency to target_currency
        pass

    def __add__(self,other):
    # add two cash class and return the sum
        return cash(0.)

# Practice 2(a): currency converting test

my_bill = cash(1000.0,'TWD')
print '>>> My bill shows',my_bill

my_bill.convert('EUR')
print '>>> After converting to EUR, my bill shows',my_bill

my_bill.convert('TWD')
print '>>> After converting to TWD, my bill shows',my_bill

# Practice 2(b): add two bills if their currencies are the same

my_bill_1 = cash(100.0,'TWD')
my_bill_2 = cash(500.0,'TWD')
print '>>> My bill #1:',my_bill_1
print '>>> My bill #2:',my_bill_2

print '>>> My bills (1+2) in total:',my_bill_1+my_bill_2

my_bill_3 = cash(50.0,'EUR')
my_bill_4 = cash(20.0,'EUR')
print '>>> My bill #3:',my_bill_3
print '>>> My bill #4:',my_bill_4

print '>>> My bills (3+4) in total:',my_bill_3+my_bill_4

# Practice 2(c): add two bills if their currencies are different

print '>>> My bills (1+4) in total:',my_bill_1+my_bill_4
print '>>> My bills (3+2) in total:',my_bill_3+my_bill_2


