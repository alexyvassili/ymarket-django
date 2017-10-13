#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Ymarket-django',
    version=0.2,
    url='https://github.com/alexyvassili/ymarket-django.git',
    license='MIT',
    author='Alexey Vasilev',
    author_email='escantor@gmail.com',
    description='',
    long_description="",
    packages=['ymarket-django'],
    include_package_data=True,
    zip_safe=False,
    platforms=' any',
    install_requires=[
        'django',
        'Pillow',
    ],

    classifiers=[

    ],
)