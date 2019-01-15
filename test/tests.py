import unittest
from validations.isdigit import is_number
from validations.isemail import emailaddress


class MyTestCase(unittest.TestCase):
    def testis_number(self):
        self.assertTrue(is_number(5))
        self.assertTrue(is_number(15))
        self.assertTrue(is_number(1568748))
        self.assertTrue(is_number(0))
        self.assertTrue(is_number(-5))
        self.assertFalse(is_number('a'))
        self.assertFalse(is_number("asdfasdf"))
        self.assertFalse(is_number('{'))

    def test_is_email(self):
        self.assertFalse(emailaddress("12fsda1234com"))
        self.assertTrue(emailaddress("12fsda@1234.com"))
        self.assertFalse(emailaddress("12fsda@1234com"))
        self.assertTrue(emailaddress("mam@kota4.com"))
        self.assertFalse(emailaddress("12fsda1234.com"))




if __name__ == '__main__':
    unittest.main()
