from setuptools import setup, find_packages

setup(
    name='some_modules',
    packages=find_packages(where='src'),
    package_dir={
        '': 'src',
    }
)
