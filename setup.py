try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Rename Files with American Style Dates to European Style Dates',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['zipfile'],
	'scripts': [],
	'name': 'Change Dates'
}

setup(**config)