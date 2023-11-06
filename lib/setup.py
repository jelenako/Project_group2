from setuptools import Extension, setup, find_packages


user_ext = Extension('pythonhashmodule', ['userlib/hash.c'])


with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()

setup(
    name='userlib',
    packages=find_packages(),
    version='3.4.5',
    long_description=long_description,
    description='user account library',
    author='Group2',
    license='MIT',
    install_requires=[],
    test_suite='tests',
    python_requires=">=3.6",
    ext_modules=[user_ext],
)
