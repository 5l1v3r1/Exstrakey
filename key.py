#!/usr/bin/python
# -*- coding: utf-8 -*-
# Exstrakey
# Coded by Senja
# Github: github.com/thedarksec/Exstrakey

import os, sys, time
from time import sleep

def banner():
    os.system('clear')
    os.system('reset')
    time.sleep(1)

banner()

def loads():
    tix = [
     '.   ', '..  ', '... ']
    for o in tix:
        print '\r\x1b[0m[\x1b[94;1m\xe2\x97\x8f\x1b[0m] \x1b[0mLoading ' + o,
        sys.stdout.flush()
        time.sleep(1)

def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

logo = """\033[77;1m
       _____         _              _____
      |   __|_ _ ___| |_ ___ ___   |  |  |___ _ _
      |   __|_'_|_ -|  _|  _| .'|  |    -| -_| | |
      |_____|_,_|___|_| |_| |__,|  |__|__|___|_  |
                                             |___|
"""
print (logo)

print ('\x1b[0m[\x1b[94;1m#\x1b[0m] \x1b[0mShorcut For Help You')
print ('\x1b[0m[\x1b[93;1m*\x1b[0m] \x1b[0mCoded by Senja')
print ('\x1b[0m[\x1b[96;1m&\x1b[0m] \x1b[0mMy Github: @thedarksec')
time.sleep(1)
print
loads()
print
print
write ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mChecking ...')
print ('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mProcess Reloads')
print
sleep (3)
write ('\x1b[0m[\x1b[93;1m!\x1b[0m] \x1b[77;1mMaking termux properties directory ...')
sleep (3)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print ('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mSuccess')
print
sleep (3)
write ('\x1b[0m[\x1b[95;1m!\x1b[0m] \x1b[77;1mMaking setup file ...')
sleep (1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','|','clear','exit'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','su','_','tor']]"
control = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
control.write(key)
control.close()
sleep (1)
print ('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mSuccess')
print
sleep (3)
write ('\x1b[0m[\x1b[97;1m!\x1b[0m] \x1b[77;1mSetting up ...')
sleep (1)
print ('\x1b[0m[\x1b[90;1m+\x1b[0m] \x1b[0mSuccesfully')
os.system('termux-reload-settings')
print
print
exit(1)
