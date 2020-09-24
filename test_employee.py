import unittest
from employee import Employee, cristina

class TestEmployee(unittest.TestCase):
    """Test for Employee class"""

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    def setUp(self):
        print('setup')
        self.levin = Employee('levin', 'batallones', 2000000)
        self.martin = Employee('martin', 'briceno', 1999999)
        self.cristina = Employee('cristina', 'nguyen', 100000)

    def tearDown(self):
        print('tearDown\n')


    def test_email(self):
        self.assertEqual(self.levin.email, 'levin.batallones@sei713.com')
        self.assertEqual(self.martin.email, 'martin.briceno@sei713.com')
        self.assertEqual(self.cristina.email, 'cristina.nguyen@sei713.com')

    def test_fullname(self):
        self.assertEqual(self.cristina.fullname, 'cristina nguyen')
    
    def test_raise_amount(self):
        
        self.cristina.apply_raise()

        self.assertEqual(self.cristina.pay, 115000)

if __name__ == '__main__':
    unittest.main()