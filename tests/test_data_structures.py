import unittest
from examples.data_structures import Stack, Queue

class StructureTests(unittest.TestCase):
    def test_stack_lifo(self):
        s = Stack(); s.push(1); s.push(2)
        self.assertEqual(s.pop(), 2); self.assertEqual(s.pop(), 1)
    def test_queue_fifo(self):
        q = Queue(); q.enqueue("a"); q.enqueue("b")
        self.assertEqual(q.dequeue(), "a"); self.assertEqual(q.dequeue(), "b")
    def test_empty_stack(self):
        with self.assertRaises(IndexError):
            Stack().pop()

if __name__ == "__main__":
    unittest.main()
