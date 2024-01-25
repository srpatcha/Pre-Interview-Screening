# test_password_validator.py
import unittest
from password_validator import validate_passwords

class TestPasswordValidator(unittest.TestCase):
    def test_validate_passwords(self):
        input_passwords = "asqwr1234@1,aF145#,2w3E*,2We3345"
        result = validate_passwords(input_passwords.split(','))
        expected_result = ['asqwr1234@1']
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()