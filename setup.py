from setuptools import setup, find_packages

setup(
    name = 'COMP30680_LAB2',
    version = '1.0',
    packages=find_packages(include=['src','src.*']),
    install_requires=[
        'psutil'
    ],
    entry_points={
        'console_script': ['my-command=src.test:main']
    }
)
