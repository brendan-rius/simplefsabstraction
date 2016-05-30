from setuptools import setup

requires = [
    'boto3'
]

setup(name='simplefsabstraction',
      version='1.0.0',
      description='A (very) simple FS/S3 abstraction',
      author='Brendan Rius',
      author_email='ping@brendan-rius.com',
      url='https://github.com/brendanrius/simplefsabstraction/',
      download_url='https://github.com/brendanrius/simplefsabstraction/tarball/1.0.0',
      packages=['simplefsabstraction'],
      keywords=['fs', 's3'],
      test_suite='tests',
      install_requires=requires)