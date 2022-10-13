import os
import sys
import unittest

import coverage


def discover_and_run(start_dir: str = '.', pattern: str = 'test*.py'):
    """Discover and run tests cases, returning the result."""
    tests = unittest.TestLoader().discover(start_dir, pattern=pattern)
    # We'll use the standard text runner which prints to stdout
    runner = unittest.TextTestRunner()
    result = runner.run(tests) # Returns a TestResult
    print(result.errors, result.failures) # And more useful properties
    return result


if __name__ == '__main__':
    result = discover_and_run()
    # cov = coverage.Coverage()
    # cov.load()
    # with open(os.devnull, "w") as f: total = cov.report(file=f)
    # print("Total: {0:.0f}".format(total))