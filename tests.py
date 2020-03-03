import sys
import unittest
import logging


def main(out=sys.stderr, verbosity=2):
    suite = unittest.TestLoader().discover(".")
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)
    


if __name__ == '__main__':
    with open('testing.log', 'a') as f:
        logging.info(format='%(asctime)s:%(levelname)s:%(message)s')
        main(f)
