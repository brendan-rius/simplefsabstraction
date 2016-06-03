from unittest import TestCase
from unittest.mock import Mock

from simplefsabstraction import S3FS


class TestS3FS(TestCase):
    def test_exists_bucket_not_found(self):
        fs = S3FS('test')
        fs._bucket_exists = Mock(return_value=False)
        with self.assertRaises(S3FS.BucketNotFoundError):
            fs.exists('hello')

    def test_save_bucket_not_found(self):
        fs = S3FS('test')
        fs._bucket_exists = Mock(return_value=False)
        with self.assertRaises(S3FS.BucketNotFoundError):
            fs.save(None, 'hello')
