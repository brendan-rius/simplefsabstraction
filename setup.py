from setuptools import setup

requires = [
    'boto3'
]

setup(name='simplefsabstraction',
      version='1.3.1',
      description='A (very) simple FS/S3 abstraction',
      author='Brendan Rius',
      author_email='ping@brendan-rius.com',
      url='https://github.com/brendan-rius/simplefsabstraction/',
      download_url='https://github.com/brendan-rius/simplefsabstraction/tarball/1.3.1',
      packages=['simplefsabstraction'],
      keywords=['fs', 's3'],
      test_suite='tests',
      install_requires=requires)
