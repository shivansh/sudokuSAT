import unittest
import grammar

class TestStringMethods(unittest.TestCase):
       def test_grammar(self):
              mat = ((2,[1,4],8),
                     (1,  2  ,3),
                     (3,  5  ,7))
              self.assertEqual(grammar.row(mat, 0, 1), True)
              self.assertEqual(grammar.row(mat, 0, 3), False)
              self.assertEqual(grammar.col(mat, 1, 1), True)
              self.assertEqual(grammar.col(mat, 1, 3), False)
              self.assertEqual(grammar.grid(mat, 0, 0, 4), True)
              self.assertEqual(grammar.grid(mat, 0, 0, 9), False)

if __name__ == '__main__':
       unittest.main()
