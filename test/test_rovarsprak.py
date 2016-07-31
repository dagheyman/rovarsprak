import unittest
from rovarsprak import parse

class TestRovarsprak(unittest.TestCase):

    def testParse(self):
        self.assertEqual(parse("rövare"), "rorövovarore")
        self.assertEqual(parse("Rövare"), "Rorövovarore")
        self.assertEqual(parse("Jag är en rövare"), "Jojagog äror enon rorövovarore")
