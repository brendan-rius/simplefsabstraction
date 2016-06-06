from unittest import TestCase

from simplefsabstraction import SimpleFS
from simplefsabstraction.local import LocalFS


class TestLocalFS(TestCase):
    def test_exists_false(self):
        local_fs = LocalFS()
        # Should work as long as nobody created that file :D
        self.assertFalse(local_fs.exists('/tmp/nonexistingfile'))

    def test_exists_true(self):
        local_fs = LocalFS()
        # Should work as long as nobody created that file :D
        self.assertTrue(local_fs.exists('/tmp/existingfile'))

    def test_allowed_extension_fails(self):
        local_fs = LocalFS()
        with self.assertRaises(SimpleFS.BadExtensionError):
            local_fs.save(None, "abc.png", extensions=['jpg'])
