import unittest
from rovarsprak import parse, unparse, verify


class TestRovarsprak(unittest.TestCase):

    def testParse(self):
        self.assertEqual(parse("rövare"), "rorövovarore")
        self.assertEqual(parse("Rövare"), "Rorövovarore")
        self.assertEqual(
            parse("Jag är en rövare"),
            "Jojagog äror enon rorövovarore")

    def testUnparse(self):
        self.assertEqual(unparse("rorövovarore"), "rövare")
        self.assertEqual(unparse("Rorövovarore"), "Rövare")
        self.assertEqual(
            unparse("Jojagog äror enon rorövovarore"),
            "Jag är en rövare")

    def testVerify(self):
        self.assertTrue(verify("rorövovarore"))
        self.assertTrue(verify("Rorövovarore"))
        self.assertTrue(verify("Jojagog äror enon rorövovarore"))
        self.assertFalse(verify("Jojagog äror enon rorövovarorer"))
        self.assertFalse(verify("rövare"))
        self.assertFalse(verify("Rövare"))
        self.assertFalse(verify("Jag är en rövare"))
