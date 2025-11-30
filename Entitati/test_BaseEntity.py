from unittest import TestCase

from Entitati.BaseEntity import BaseEntity


class TestBaseEntity(TestCase):
    def setUp(self):
        self.b = BaseEntity(1)
        self.b1 = BaseEntity(2)

    def test_get_id(self):
        self.assertEqual(self.b.getID(),1)


    def test_set_id(self):
        self.b.setID(2)
        self.assertEqual(self.b.getID(),self.b1.getID())

    def test_str(self):
        self.assertEqual(str(self.b),str(1))
        self.assertEqual(str(self.b1),str(2))
