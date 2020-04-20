# from .servoserial import ServoSerial
# from .ax12 import AX12
# from .xl320 import XL320
# from .xl430 import XL430
try:
    from importlib.metadata import version # type: ignore
except ImportError:
    from importlib_metadata import version # type: ignore

__copyright__ = 'Copyright (c) 2016 Kevin Walchko'
__license__ = 'MIT'
__author__ = 'Kevin J. Walchko'
__version__ = version("pyservos")
