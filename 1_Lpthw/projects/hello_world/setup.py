try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'First Project',
    'author': 'pandoraemon',
    'url':'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'pz880304@163.com',
    'version': '0.1',
    'install_requires':['nose'],
    'package': ['hello'],
    'scripts': [],
    'name': 'hello_world'
}

setup(**config)
