from odoo.tests.common import TransactionCase
from odoo.tests import tagged


@tagged('demo')
class TestSampleClass(TransactionCase):
    def test_001(self):
        self.assertEqual(1, 1)
    

@tagged('demo')
class TestSampleClass02(TransactionCase):
    def test_002(self):
        self.assertEqual(1, 1)

    def test_003(self):
        self.assertEqual(1, 1)
    
    def test_004(self):
        self.assertEqual(1, 1)
