from distutils.core import setup, Extension

module = Extension('pythonhashmodule', sources=['hash.c'])

setup(name='pythonhashmodule',
      version='1.0',
      description='Python module for password hashing',
      ext_modules=[module])

