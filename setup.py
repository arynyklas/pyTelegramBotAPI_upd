#!/usr/bin/env python3


from setuptools import setup
from io import open
import re


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

with open('telebot/version.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$", f.read(), flags=re.MULTILINE).group(1)

setup(
    name='pyTelegramBotAPI',
    version=version,
    description='Library for interaction with Telegram Bot API.',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='arynyklas',
    author_email='arynyklas@gmail.com',
    url='https://github.com/arynyklas/pyTelegramBotAPI_upd',
    packages=['telebot'],
    license='GPL2',
    keywords='telegram bot api tools',
    install_requires=['requests'],
    extras_require={
        'redis': 'redis>=3.4.1'
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ]
)