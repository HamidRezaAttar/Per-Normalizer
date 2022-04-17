from setuptools import setup, find_packages

setup(
    name='per-normalizer',
    version='0.1.0',
    license='MIT',
    author="HamidReza Attar",
    author_email='hamidattar5@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/HamidRezaAttar/Per-Normalizer',
    keywords='Normalizer',
    install_requires=[
        'parsivar',
    ],

)
