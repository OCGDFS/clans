"""
Phusion Passenger WSGI entrypoint
"""

import sys

if sys.version_info.major != 3:
    raise RuntimeError(
        "FAForever API requires python 3.\n"
        "Refer to passenger documentation on how to accomplish that.\n"
        "Good luck.")

from app import app as application
