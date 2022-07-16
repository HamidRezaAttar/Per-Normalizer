
import codecs
from os import path
from setuptools import setup


setup(
	name='pernorm',
	version='0.0.2',
	description='Persian Normalizer',
	author='HamidReza Attar',
	author_email='hamidattar5@gmail.com',
	url='https://github.com/HamidRezaAttar/Per-Normalizer',
	long_description="A Python library for Persian text preprocessing.",
	long_description_content_type='text/markdown',
	packages=['pernorm'],
 	keywords=['python', 'persian', 'normalizer', 'text'],
	classifiers=[
		'Topic :: Text Processing',
		'Natural Language :: Persian',
		'Programming Language :: Python :: 3',
	],
	install_requires=['parsivar==0.2.3'],
)