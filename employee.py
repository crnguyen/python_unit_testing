class Employee:
    """ a sample employee class"""

    raise_amount = 1.15

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)

    @property
    def email(self):
        return'{}.{}@sei713.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = round(float(self.pay * self.raise_amount))

cristina = Employee('cristina', 'nguyen', '100000')

# print(cristina.email)
# print(cristina.fullname)
# print()