from os import path
from io import open

from setuptools import setup
from setuptools import find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='mimir',
    version='2.0.0',
    description='Smart OSINT collection and enrichment',

    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/deadbits/mimir',
    author='Adam M. Swanda',
    author_email='adam@deadbits.org',

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='osint cybersecurity infosec spamlists reputationdbs',

    packages=find_packages(exclude=['mimir/data/docs']),

    python_requires='>=3.7',

    install_requires=[
        'requests',
        'configparser',
        'validators',
        'colorama',
        'pygments',
        'urllib3',
        'dnspython',
        'shodan'
        'whois',
        'pymisp',
        'spam-list',
        'datetime',
        'maxminddb'
    ],

    package_data={
        'mimir': [
            'mimir/data/apikeys.json.example',
            'mimir/maxmind/*',
            'mimir/data/logo/mimir.png'
        ],
    },

    data_files=[
        ('mimir',
            [
                'mimir/data/apikeys.json.example',
                'mimir/data/maxmind/*',
                'mimir/data/extra/logo/minir-logo.png'
            ]
        )
    ],

    entry_points={
        'console_scripts': [
            'mimir=mimir.mimir:main',
        ],
    },

    project_urls={
        'Bug Reports': 'https://github.com/deadbits/mimir/issues',
        'Say Thanks!': 'http://saythanks.io/to/deadbits',
        'Source': 'https://github.com/deadbits/mimir/',
    },
)

