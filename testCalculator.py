import unittest
import mortgageCalculator

class test_monthly_payment(unittest.TestCase):
    """
    def test_monthlyPayment(self):
        monthlyPayment = mortgageCalculator.loanAmount(344000)
        self.assertAlmostEqual(monthlyPayment,2566.128476787066)
    """
    def test_monthlyPayment(self):
        monthlyPayment = mortgageCalculator.loanAmount(2000)
        self.assertEqual(monthlyPayment,2566.13)

    def test_stateInterestRate(self):
        testValue = mortgageCalculator.stateRate()
        message = 'Test Value is not true'
        self.assertTrue(testValue, message)
#Executing Test Runners
if __name__ == '__main__':
    #This is a command line entry point. It means that if you execute the script alone by running python test.py at the command line, it will call unittest.main(). This executes the test runner by discovering all classes in this file that inherit from unittest.TestCase.
    unittest.main()
