import os
from shutil import copyfile

from simplefsabstraction.interface import SimpleFS


class LocalFS(SimpleFS):
    """
    The local file system
    """

    def exists(self, file_name):
        return os.path.isfile(file_name)

    def save(self, source_file, dest_name):
        copyfile(source_file, dest_name)
