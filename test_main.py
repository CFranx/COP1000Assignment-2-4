import unittest
import main

class TestMain(unittest.TestCase):
  def test_input1(self):
    result = main.salaryDependents()
    self.assertEqual(result, ("State Tax: $3900.0","Federal Tax: $16800.0","Dependents: $4500.0","Salary: $60000.0","Take Home Pay: $34800.0"))

  def test_input2(self):
    result = main.salaryDependents()
    self.assertEqual(result, ("State Tax: $1950.0","Federal Tax: $8400.0","Dependents: $4500.0","Salary: $30000.0","Take Home Pay: $15150.0"))

if __name__ == "__main__":
  unittest.main()