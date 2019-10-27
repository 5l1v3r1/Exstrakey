#!/usr/bin/python
# Life Of Programmer
# Coded By Nedi Senja

import os, sys, time
from time import sleep

def banner():
    os.system('clear')
    os.system('reset')
    time.sleep(1)

banner()

def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

logo = """

\x1b[94;2;3m  ████████╗███████╗██████╗ \x1b[93;2;3m███╗   ███╗██╗   ██╗██╗  ██╗
\x1b[94;2;3m  ╚══██╔══╝██╔════╝██╔══██╗\x1b[93;2;3m████╗ ████║██║   ██║╚██╗██╔╝
\x1b[94;2;3m     ██║   █████╗  ██████╔╝\x1b[93;2;3m██╔████╔██║██║   ██║ ╚███╔╝
\x1b[94;2;3m     ██║   ██╔══╝  ██╔══██╗\x1b[93;2;3m██║╚██╔╝██║██║   ██║ ██╔██╗
\x1b[94;2;3m     ██║   ███████╗██║  ██║\x1b[93;2;3m██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
\x1b[94;2;3m     ╚═╝   ╚══════╝╚═╝  ╚═╝\x1b[93;2;3m╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝
"""
print (logo)
print ('')

print
print ('\x1b[0m[\x1b[92;1m#\x1b[0m] \x1b[0mShorcut for help you')
print ('\x1b[0m[\x1b[95;1m*\x1b[0m] \x1b[0mCoded by Nedi Senja')
time.sleep(1)
print ('')

write ('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mChecking ...')
print ('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mProcess Reloads')
print ('')
sleep (3)
write ('\x1b[0m[\x1b[93;1m!\x1b[0m] \x1b[77;1mMaking termux properties directory ...')
sleep (3)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print ('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mSuccess')
print ('')
sleep (3)
write ('\x1b[0m[\x1b[95;1m!\x1b[0m] \x1b[77;1mMaking setup file ...')
sleep (1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','|','clear','exit'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','su','_','tor']]"
control = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
control.write(key)
control.close()
sleep (1)
print ('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mSuccess')
print ('')
sleep (3)
write ('\x1b[0m[\x1b[97;1m!\x1b[0m] \x1b[77;1mSetting up ...')
sleep (1)
print ('\x1b[0m[\x1b[90;1m+\x1b[0m] \x1b[0mSuccesfully')
os.system('termux-reload-settings')
print ('')
print ('')
exit(1)
