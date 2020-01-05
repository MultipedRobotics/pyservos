##############################################
# The MIT License (MIT)
# Copyright (c) 2016 Kevin Walchko
# see LICENSE for full details
##############################################

from __future__ import print_function
from setuptools import setup
# from pyservos import __version__ as VERSION
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution
from build_utils import SetGitTag
from build_utils import get_pkg_version


PACKAGE_NAME = 'pyservos'
VERSION = get_pkg_version('pyservos/__init__.py')
BuildCommand.pkg = PACKAGE_NAME
BuildCommand.py2 = False  # not supporting python2 anymore
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION
SetGitTag.version = VERSION


setup(
    author='Kevin Walchko',
    author_email='walchko@users.noreply.github.com',
    name=PACKAGE_NAME,
    version=VERSION,
    description='A library to control dynamixel AX-12 and XL-320 servos with python',
    long_description=open('readme.md').read(),
    url='http://github.com/walchko/{}'.format(PACKAGE_NAME),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
    license='MIT',
    keywords=['dynamixel', 'robotis', 'ax12', 'ax-12', 'ax-12a', 'xl320', 'xl-320', 'servo', 'actuator', 'library', 'robotics', 'robot', 'smart', 'spider'],
    packages=[PACKAGE_NAME],
    # install_requires=open('requirements.txt').readlines(),
    extras_require={
        'GPIO': ['RPi.GPIO']
    },
    install_requires=[
        'pyserial',
        'build_utils',
        'linuxinfo'
        # 'RPi.GPIO'
    ],
    cmdclass={
        'publish': PublishCommand,
        'make': BuildCommand
    },
    scripts=[
        'bin/set_id.py',
        'bin/servo_ping.py',
        'bin/set_angle.py',
        # 'bin/set_baud_rate.py',
        # 'bin/servo_reboot.py',
        # 'bin/servo_reset.py',
        # 'bin/get_angle.py'
    ]
)
