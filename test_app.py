import unittest


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(sum([2,6]),8,'Should be 8')


if __name__ == '__main__':
    unittest.main()
