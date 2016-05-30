from unittest import TestCase

from simplefsabstraction.local import LocalFS


class TestLocalFS(TestCase):
    def setUp(self):
        self.local_fs = LocalFS()

    def test_exists_false(self):
        # Should work as long as nobody created that file :D
        self.assertFalse(self.local_fs.exists('/tmp/nonexistingfile'))

    def test_exists_true(self):
        # Should work as long as nobody created that file :D
        self.assertTrue('/tmp/existingfile')
