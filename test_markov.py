import unittest
#from markov import Markov, get_table
import markov as mk

class TestMarkov(unittest.TestCase):
    def test_markov(self):
        m = mk.Markov('ab')
        res = m.predict('a')
        self.assertEqual(res, 'b')

    def test_markov2(self):
        m = mk.Markov('abc', size = 2)
        res = m.predict('ab')
        self.assertEqual(res, 'c')

    def test_get_table(self):
        res = mk.get_table('ab')
        self.assertEqual(res,{'a':{'b':1}})

    def test_get_table2(self):
        res = mk.get_table('abc',
                           size=2)
        self.assertEqual(res,
                         {'ab': {'c':1}})                      

if __name__ == '__main__':
    print(f"unitest executing as {__name__}")
    unittest.main()
