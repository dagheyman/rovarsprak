import unittest
from rovarsprak import parse, unparse

class TestRovarsprak(unittest.TestCase):

    def testParse(self):
        self.assertEqual(parse("rövare"), "rorövovarore")
        self.assertEqual(parse("Rövare"), "Rorövovarore")
        self.assertEqual(parse("Jag är en rövare"), "Jojagog äror enon rorövovarore")

    def testUnparse(self):
        self.assertEqual(unparse("rorövovarore"), "rövare")
        self.assertEqual(unparse("Rorövovarore"), "Rövare")
        self.assertEqual(unparse("Jojagog äror enon rorövovarore"), "Jag är en rövare")
