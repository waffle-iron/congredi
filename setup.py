# WARNING - sync congredi/setup.py and congredi/delegito/setup.py
from setuptools import setup
def readme():
    with open('README.md') as f:
        return f.read()
setup(name='delegito',
    version='0.0',
    description='Single Transferable Voting service',
    long_description='Delegito is the python module for an STV API called congredi.\
    This is currently a work in progress, so the Shuffle-Sum & Secure Secret Sharing\
    are not implemented as directly as need be. I\'m also terrible at interfaces...', #readme()
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Topic :: Security :: Cryptography'
        ],
    keywords='STV Single Transferable Voting',
    url='https://github.com/thetoxicarcade/congredi',
    author='Cameron Whiting',
    author_email='thetoxicarcade@gmail.com',
    license='GPL3',
    packages=['delegito'],
    install_requires=[
        'flask',
        'redis',
        'celery',
        'pymongo',
        'PGPy',
        'stem',
        'pyjwt'
        ],
    include_package_data=True,
    test_suite='nose2.collector.collector',
    tests_require=['nose2'],
    zip_safe=False
    )
#python setup.py register sdist upload