from odoo.tests.common import TransactionCase
from odoo.tests import tagged


@tagged('demo')
class TestSampleClass(TransactionCase):
    def test_01(self):
        self.assertEqual(1, 1)
    

@tagged('demo')
class TestSampleClass02(TransactionCase):
    def test_02(self):
        self.assertEqual(1, 1)

    def test_03(self):
        self.assertEqual(1, 1)
    
    def test_04(self):
        self.assertEqual(1, 1)
