#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import config
from notmain import set_globvar_to_one

def print_globvar():
	print config.globvar

set_globvar_to_one()
print_globvar()       # Prints 1
