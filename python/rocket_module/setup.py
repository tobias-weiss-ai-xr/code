"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rocketlauncher',
    version='0.0.1',
    description='rocketlauncher with cmd, gui and TCP server',
    url='https://www.tobias-weiss.org',
    author='Tobias Weiss',
    author_email='spam@tobias-weiss.org',
    license='MIT',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='usb rocketlauner dreamjerkey',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    #install_requires=['peppercorn'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    data_files=[
        ('defaults', ['data/defaults.cfg'])
        ('facedetect', ['data/haarcascade_frontalface_default.xml'])
        ],

    entry_points={
        'console_scripts': [
            'rocket_cmd=rocket.rocket_cmd:main',
            'rocket_gui=rocket.rocket_gui:main',
        ],
    },
)
