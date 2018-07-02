#!./venv/bin/python
from distutils.core import setup

setup(
    name = 'Address book',
    version = '1.0',
    author = 'Rafael F Filho',
    url = 'https://github.com/rafaelffilho/addressbook',
    install_requires = ['requests', 'python-firebase']
)
