import sys
import unittest


def main(out=sys.stderr, verbosity=2):
    suite = unittest.TestLoader().discover(".")

    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    with open('testing.log', 'w') as f:
        main(f)
