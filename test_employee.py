import unittest
from employee import Employee, cristina

class TestEmployee(unittest.TestCase):
    """Test for Employee class"""

    def test_email(self):
        levin = Employee('levin', 'batallones', 2000000)
        martin = Employee('martin', 'briceno', 1999999)

        self.assertEqual(levin.email, 'levin.batallones@sei713.com')
        self.assertEqual(martin.email, 'martin.briceno@sei713.com')
        self.assertEqual(cristina.email, 'cristina.nguyen@sei713.com')

if __name__ == '__main__':
    unittest.main()