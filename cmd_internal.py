#!/usr/bin/python
#
# Copyright (c) 2010-2012 Liraz Siri <liraz@turnkeylinux.org>
#
# This file is part of TKLBAM (TurnKey GNU/Linux BAckup and Migration).
#
# TKLBAM is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of
# the License, or (at your option) any later version.
#
"""
Execute an internal command
"""
import os
from cliwrapper import CliWrapper

import cmd_internals

class CliWrapper(CliWrapper):
    DESCRIPTION = __doc__
    PATH = cmd_internals.__path__

main = CliWrapper.main

if __name__ == "__main__":
    CliWrapper.main()


