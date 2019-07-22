import unittest
from pyds.LinkedLists import Singlellist


class testSinglellist(unittest.TestCase):
    def test_init_items(self):
        sll = Singlellist([1, 2, 3])
        self.assertEqual(len(sll), 3)
        self.assertEqual(sll.head.value, 1)
        self.assertEqual(sll.tail.value, 3)
        self.assertEqual(str(sll), 'SLL[1, 2, 3]')

    def test_contains(self):
        sll = Singlellist()
        self.assertNotIn(1, sll)
        sll = Singlellist([1, 2, 3])
        self.assertIn(1, sll)
        self.assertNotIn(0, sll)
        self.assertNotIn('0', sll)

    def test_empty(self):
        sll = Singlellist()
        self.assertEqual(sll.is_empty(), True)
        sll.add_first(1)
        self.assertEqual(sll.is_empty(), False)

    def test_add_first(self):
        sll = Singlellist()
        self.assertEqual(sll.head, None)
        sll.add_first(1)
        self.assertEqual(sll.head.value, 1)
        sll.add_first(2)
        self.assertEqual(sll.head.value, 2)

    def test_add_last(self):
        sll = Singlellist()
        self.assertEqual(sll.tail, None)
        sll.add_last(1)
        self.assertEqual(sll.tail.value, 1)
        sll.add_last(2)
        self.assertEqual(sll.tail.value, 2)

    def test_insert_after(self):
        sll = Singlellist([1, 2, 3])
        sll.insert_after(1, 11)
        self.assertEqual(sll[1], 11)
        sll.insert_after(3, 33)
        self.assertEqual(sll[4], 33)

    def test_remove_first(self):
        sll = Singlellist([1, 2, 3])
        sll.remove_first()
        self.assertEqual(sll[0], 2)
        sll.remove_first()
        self.assertEqual(sll[0], 3)
        sll.remove_first()
        self.assertEqual(sll.is_empty(), True)

    def test_remove_last(self):
        sll = Singlellist([1, 2, 3])
        sll.remove_last()
        self.assertEqual(sll[1], 2)

    def test_remove(self):
        sll = Singlellist([1, 2, 3])
        sll.remove(1)
        self.assertEqual(sll.head.value, 2)
        sll.remove(3)
        self.assertEqual(sll.tail.value, 2)

    def test_remove_all(self):
        sll = Singlellist([1, 1, 2, 3, 3])
        sll.remove_all(1)
        self.assertEqual(str(sll), "SLL[2, 3, 3]")
        sll.remove_all(3)
        self.assertEqual(str(sll), "SLL[2]")
        sll.remove_all(2)
        self.assertEqual(sll.is_empty(), True)

    def test_change(self):
        sll = Singlellist([1, 2, 3])
        sll.change(1, 0)
        self.assertEqual(sll.head.value, 0)
        sll.change(3, 4)
        self.assertEqual(sll.tail.value, 4)

    def test_change_all(self):
        sll = Singlellist([1, 1, 2, 3, 3])
        sll.change_all(1, 0)
        self.assertEqual(str(sll), "SLL[0, 0, 2, 3, 3]")
        sll.change_all(3, 4)
        self.assertEqual(str(sll), "SLL[0, 0, 2, 4, 4]")

    def test_search(self):
        sll = Singlellist([1, 2, 3])
        self.assertTrue(1 in sll)
        self.assertFalse(0 in sll)
