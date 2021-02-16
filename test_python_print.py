#!/usr/bin/env python
# initially to be a python script to print multiple pdf files in a folder
# aside from assembling the needed modules and learning how to use their methods
# ghostscript (gswin64c.exe) was installed in windows 10 along with GhostView
# initially the printing was proven on one file from an Administrative Command prompt window
# this proved printing to a named printer and shrinking the content so the borders would
# not be cut off
#
import glob
import win32.win32print
import win32.win32api as win32api
# import win32printing
# print(glob.glob("/home/adam/*.pdf"))
# print(glob.glob("./*.pdf"))
alist = (glob.glob("./*.pdf"))

# this works from the command line, command window opened as administrator
# in the C:\Program Files\gs\gs9.53.3\bin directory
# C:\Program Files\gs\gs9.53.3\bin>gswin64c.exe -sDEVICE=mswinpr2 -dBATCH -dNOPAUSE -sOutputFile="%printer%Canon MF220 Series V4" test.pdf
# when printing with the above, the tops of pages got cut off so the contents needed to be shrunk to the printable area of the page
# this is a setting in the Adobe printing window and the setting for the same, using gs was found on stackoverflow
# C:\Program Files\gs\gs9.53.3\bin>gswin64c.exe -sDEVICE=mswinpr2 -dBATCH -dNOPAUSE -dPDFFitPage -sOutputFile="%printer%Canon MF220 Series V4" test.pdf
# here's the stack overflow link:
# https://stackoverflow.com/questions/22138567/shrink-pdf-to-fit-onto-one-page-using-ghostscript


# for i in alist:
#   print(str(i))

# functions_list = dir(win32printing)
# print(functions_list)


GHOSTSCRIPT_PATH = "C:\\Program Files\\gs\\gs9.53.3\\bin\\gswin64.exe"
# GHOSTSCRIPT_PATH = "C:\Program Files\gs\gs9.53.3\bin\

GSPRINT_PATH = "C:\\Program Files\\Ghostgum\\gsview\\gsprint.exe"

currentprinter = win32.win32print.GetDefaultPrinter()
# currentprinter = "Canon MF220 Series V4"
# print(currentprinter)

params = '-ghostscript "'+ GHOSTSCRIPT_PATH  +'" -printer "'+currentprinter+'" "test.pdf "'
# print(params)

# win32api.ShellExecute(0, 'open', GSPRINT_PATH, params, '.',0)
# win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "C:\Users\Dave Neill\Downloads\clcwest\OneDrive\3-3-21\3-3-21\test.pdf"', '.', 0)
win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "test.pdf"', '.', 0)

## win32api.ShellExecute(0, print, 'test.pdf', '/d:%s' % currentprinter, ., 0)
