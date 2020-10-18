import unittest
import os

# Load Test Modules
from test import (
    test_task,
    test_genesis,
    test_schemas_network
)

# Creates loader and empty test suite.
loader = unittest.TestLoader()
suite = unittest.TestSuite()



def load_tests():
    suite.addTests(loader.loadTestsFromModule(test_task))
    suite.addTests(loader.loadTestsFromModule(test_genesis))
    suite.addTests(loader.loadTestsFromModule(test_schemas_network))


def run_tests():
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suite)


if __name__ == "__main__":
    load_tests()
    run_tests()
