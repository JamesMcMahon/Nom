#!/usr/bin/env python
from distutils.core import setup

setup(
	name='nom',
	version='0.1',
	packages=['nom'],
	entry_points={
		'console_scripts': [
			'nom = nom.main:main',
		]
	},
)
