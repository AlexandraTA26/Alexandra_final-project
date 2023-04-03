import unittest

from subscribe import Subscribe
from buton_login import Login
from search import Search
"""
1. pip install html-testRunner
2. Din python packeges

"""
import HtmlTestRunner

class TestSuite(unittest.TestCase):

    def test_suite(self):
        test_de_rulat = unittest.TestSuite()
        test_de_rulat.addTests([
                                unittest.defaultTestLoader.loadTestsFromTestCase(Subscribe),
                                unittest.defaultTestLoader.loadTestsFromTestCase(Search),
                                unittest.defaultTestLoader.loadTestsFromTestCase(Login)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title= "Test Execution Report",
            report_name= "Test Results"
        )

        runner.run(test_de_rulat)
