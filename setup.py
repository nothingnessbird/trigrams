from setuptools import setup

setup(
    name='trigrams',
    description='put some stuff here',
    author='Kinley Ramson and Chelsea Dole',
    author_emails='kinleyramson@gmail.com, chelseadole@gmail.com',
    package_dir={'': 'src'},
    py_modules=['trigrammer'],
    install_requires=['ipython'],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'pytest-watch']
    },
    entry_points={
        'console_scripts': [
            'runme=trigram:trigrammer'
        ]
    }
)
