#!/usr/bin/env python
try:
	from setuptools import setup
except ImportError:
	"""	
	I am still trying to make sense of this ez_setup stuff
	commenting it out for now

	from ez_setup import use_setuptools
	use_setuptools()
	from setuptools import setup
	"""

setup(
	name='nom',
	version='0.1',
	url="https://github.com/JamesMcMahon/nom",
	license="MIT License",
	author="James McMahon",
	description="Simple app to store configuration files",
	packages=['nom'],
	requires=('GitPython (>=0.3.1)',),
	entry_points={
		'console_scripts': [
			'nom = nom.main:main',
		]
	},
)
