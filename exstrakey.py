#!/data/data/com.termux/files/usr/bin/python
# -*- coding: utf-8 -*-
# Exstrakey
# Coded by Senja
# Github: https://github.com/stepbystepexe/Exstrakey
from __opt__ import *
import os, sys, time, marshal
from time import sleep
os.system('clear')
os.system('reset')
time.sleep(1)
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
print
print (logo)
print ('\x1b[0;43;90;1m[         Exstra Key v1.0, Coded by @stepbystep          ]\x1b[0m\n')
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
key = "extra-keys = [['ESC','/','-','HOME','UP','END','ENTER','clear','exit'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','F1','DEL','tor']]"
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
