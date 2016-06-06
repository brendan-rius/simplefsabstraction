from unittest import TestCase

from simplefsabstraction import SimpleFS


class TestSimpleFS(TestCase):
    def test_allowed_extension_fails(self):
        self.assertFalse(SimpleFS._check_extension('abc.png', ['jpg']))

    def test_allowed_extension_succeed(self):
        self.assertTrue(SimpleFS._check_extension('abc.png', ['png']))
