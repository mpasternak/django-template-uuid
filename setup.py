#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = ['django',]

setup(
    name='django_template_uuid',
    version='0.0.1',
    description="Generate UUIDs for Django templates",
    author="Michał Pasternak",
    author_email='michal.dtz@gmail.com',
    url='https://github.com/mpasternak/django-template-uuid',
    packages=find_packages(),
    install_requires=requirements,
    license="MIT license",
    zip_safe=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
