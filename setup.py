#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('docs/HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['Click', 'typer' ]

test_requirements = ['pytest>=3', ]

setup(
    author="Weibo Ren",
    author_email='renweibo@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'gitOgit=gitOgit.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gitOgit',
    name='gitOgit',
    packages=find_packages(include=['gitOgit', 'gitOgit.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/renweibo/gitOgit',
    version='0.1.1',
    zip_safe=False,
)
