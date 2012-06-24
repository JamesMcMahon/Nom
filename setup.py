#!/usr/bin/env python
from distutils.core import setup

setup(
	name='nom',
	version='0.1',
	url="https://github.com/JamesMcMahon/nom",
	license="MIT License",
	author="James McMahon",
	description="Simple app to store configuration files",
	packages=['nom'],
	entry_points={
		'console_scripts': [
			'nom = nom.main:main',
		]
	},
)
