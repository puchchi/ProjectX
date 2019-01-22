#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "ProjectX.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
