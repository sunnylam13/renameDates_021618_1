try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Rename Files with American Style Dates to European Style Dates',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/renameDates_021618_1',
	'download_url': 'https://github.com/sunnylam13/renameDates_021618_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['zipfile'],
	'scripts': [],
	'name': 'Change American to European Dates'
}

setup(**config)