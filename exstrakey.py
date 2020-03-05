#!/usr/bin/python
# -*- coding: utf-8 -*-
# Exstrakey
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Exstrakey

import os, sys, time, random
from time import sleep

info = """
Nama        : Exstrakey
Versi       : 2.2 (Update: 26 Januari 2020, 8:00 AM)
Tanggal     : 15 Juli 2019
Author      : Nedi Senja
Tujuan      : Menampilkan keyboard plus
              untuk bantu para nob seperti saya
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;43;90;1m[          Exstrakey, My Github: @stepbystepexe          ]\033[0m"""

logo = """
  \033[0;35m█▀▀▀▀ █   █ █▀▀▀▀ ▀▀█▀▀ █▀▀▀▄ █▀▀▀█ \033[0;37m█   █ █▀▀▀▀ █   █
  \033[0;35m█▀▀▀  ▄▀▀▀▄ ▀▀▀▀█   █   █▀▀▀▄ █▀▀▀█ \033[0;37m█▀▀▀▄ █▀▀▀  ▀▀█▀▀
  \033[0;35m▀▀▀▀▀ ▀   ▀ ▀▀▀▀▀   ▀   ▀   ▀ ▀   ▀ \033[0;37m▀   ▀ ▀▀▀▀▀   ▀
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def loads():
    o = [' .   ',' ..  ',' ... ']
    for i in o:
        print('\r\033[0m[\033[0;34m●\033[0m] Loading'+i,end=''),;sys.stdout.flush();time.sleep(1)

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def usage():
    os.system('clear')
    os.system('reset')
    time.sleep(1)
    print()
    print(logo)
    print(example)
    print()
    write("\033[0m[ \033[32mINFO \033[0m] \033[3mSaya tidak real kalo code program saya ini ditiru")
    write("         Seburuk apaun itu tolong hargai karya milik orang\033[0m\n")
    print()
    loads()
    sleep(1)
    print()
    print()
    write('\x1b[0m[\x1b[91;1m!\x1b[0m] \x1b[77;1mMengecek ...')
    print('\x1b[0m[\x1b[92;1m+\x1b[0m] \x1b[0mProses Penginstalan')
    print()
    sleep(3)
    write('\x1b[0m[\x1b[93;1m!\x1b[0m] \x1b[77;1mMembuat properti folder termux ...')
    sleep(3)
    try:
          os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
          pass
    print('\x1b[0m[\x1b[94;1m+\x1b[0m] \x1b[0mSukses')
    print()
    sleep(3)
    write('\x1b[0m[\x1b[95;1m!\x1b[0m] \x1b[77;1mMembuat setup file ...')
    sleep(3)
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','ENTER','clear','exit'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','F1','DEL','tor']]"
    control = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
    control.write(key)
    control.close()
    sleep(3)
    print('\x1b[0m[\x1b[96;1m+\x1b[0m] \x1b[0mSukses')
    print()
    sleep(3)
    write('\x1b[0m[\x1b[97;1m!\x1b[0m] \x1b[77;1mMenyetel ...')
    sleep(3)
    print('\x1b[0m[\x1b[90;1m+\x1b[0m] \x1b[0mBerhasil Semua')
    os.system('termux-reload-settings')
    print()
    print()
    input('[ Tekan Enter ]')
    restart()

os.system('clear')
os.system('reset')
sleep(1)
print()
print(logo)
print(example)
print()
print("\033[0m[\033[1;96;2m1\033[0m] \033[1;77mGunakan Exstrakey")
print()
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print()
option = input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
if option.strip() in '1 gunakan'.split():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    usage()
elif option.strip() in '& 2 lisensi'.split():
    print()
    os.system('nano LICENSE')
    print()
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant ExtraKey')
    print(info)
    sleep(1)
    print()
    input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print()
    os.system('git pull origin master')
    print()
    input('\033[0m[ \033[32mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- 0 keluar'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print()
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print()
    sleep(1)
    restart()
