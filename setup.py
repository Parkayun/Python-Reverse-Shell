# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

FILE = 'rs.py'

excludes = [
    "pywin",
    "pywin.debugger",
    "pywin.debugger.dbgcon",
    "pywin.dialogs",
    "pywin.dialogs.list",
    "win32com.server",
]

options = {
    "bundle_files": 1,                 
    "compressed"  : 1,                
    "excludes"    : excludes, 
    "dll_excludes": ["w9xpopen.exe"]   
}

setup(
    options = {"py2exe": options},
    zipfile = None,                    
    windows = [FILE]
)
