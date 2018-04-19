.. image:: https://raw.githubusercontent.com/MomsFriendlyRobotCompany/pyservos/master/pics/complex.gif
    :align: center
    :width: 300px
    :target: https://github.com/MomsFriendlyRobotCompany/pyservos
    :alt: animated gif

pyServos
=========

.. image:: https://img.shields.io/pypi/v/pyservos.svg
    :target: https://pypi.python.org/pypi/pyservos/
    :alt: Latest Version
.. image:: https://img.shields.io/pypi/l/pyservos.svg
    :target: https://pypi.python.org/pypi/pyservos/
    :alt: License
.. image:: https://travis-ci.org/MomsFriendlyRobotCompany/pyservos.svg?branch=master
    :target: https://travis-ci.org/MomsFriendlyRobotCompany/pyservos


**Still under development**

This is still a work in progress and **only** supports AX-12A and XL-320. The
library is divided up as follows:

 - pyservos
 	- **ServoSerial** - half duplex hardware serial interface
	- **Packet** - creates packets to talk to the servo
	- **utils** - misc
	- **XL320** - register/command/error definitions for Dynamixel's XL-320 servo
	- **AX12** - register/command/error definitions for Dynamixel's AX-12A servo


Setup
--------

Install
~~~~~~~~~~~~~

The suggested way to install this is via the ``pip`` command as follows::

	pip install pyservos

Development
~~~~~~~~~~~~~

To submit git pulls, clone the repository and set it up as follows::

	git clone https://github.com/walchko/pyservos
	cd pyservos
	pip install -e .

Usage
--------

The ``\bin`` directory has a number of useful programs to set servo position or ID number. Just
run the command with the ``--help`` flag to see how to use it.

==================== ==============================================================
Command              Description
==================== ==============================================================
``servo_ping.py``    pings one or all of the servos
``servo_reboot.py``  reboots one or all servos
``servo_reset.py``   resets one or all servos to a specified level
``set_angle.py``     sets the angle of a given servo
``set_baud_rate.py`` change the baud rate of the servos
``set_id.py``        changes the ID number for a given servo
==================== ==============================================================

Documentation
-------------------------------------------------------------------------------------

- `AX-12A Servo <https://github.com/MomsFriendlyRobotCompany/pyservos/tree/master/docs/ax12>`_
- `XL-320 Servo <https://github.com/MomsFriendlyRobotCompany/pyservos/tree/master/docs/xl320>`_

A simple example to turn the servo and turn the LED on using a USB serial converter:

.. code-block:: python

	# Run an AX-12 servo
	from pyservos import ServoSerial, Packet, AX12

	serial = ServoSerial('/dev/tty.usbserial')  # tell it what port you want to use
	# serial = ServoSerial('dummy')  # use a dummy serial interface for testing
	serial.open()

	ax = Packet(AX12)
	pkt = ax.makeServoPacket(1, 158.6)  # move servo 1 to 158.6 degrees
	ret = serial.sendPkt(pkt)  # send packet, I don't do anything with the returned status packet

	pkt = ax.makeLEDPacket(1, AX12.LED_ON)
	ret = serial.sendPkt(pkt)

Although I have made some packet creators (like LED and Servo), you can make
your own using the basic ``makeWritePacket`` and ``makeReadPacket``.

.. code-block:: python

	# Run an XL-320 servo
	from pyservos import Packet, XL320
	from pyservos.utils import angle2int

	xl = Packet(XL320)

	# let's make our own servo packet that sends servo 3 to 220.1 degrees
	ID = 3
	reg = XL320.GOAL_POSITION
	params = angle2int(220.1)  # convert 220.1 degrees to an int between 0-1023
	pkt = xl.makeWritePacket(ID, reg, params)

Robot Examples
------------------

Here are some example `robots <https://github.com/MomsFriendlyRobotCompany/pyservos/tree/master/docs/robots>`_

Change Log
-------------

========== ======= =============================
2018-02-17 1.0.0   added AX-12 support and renamed the library
2017-04-01 0.9.0   added python3 support
2017-03-26 0.8.0   major overhaul and removed the GPIO stuff
2017-03-19 0.7.7   can switch between GPIO pin and pyserial.setRTS()
2017-02-20 0.7.6   small fixes and added servo_reboot
2017-01-16 0.7.5   fixes some small errors
2016-11-29 0.7.4   add bulk write and small changes
2016-10-11 0.7.1   small changes/updates
2016-09-12 0.7.0   refactoring, still working on API
2016-09-05 0.5.0   published to PyPi
2016-08-16 0.0.1   init
========== ======= =============================

Software License
------------------------

**The MIT License (MIT)**

Copyright (c) 2016 Kevin J. Walchko

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
