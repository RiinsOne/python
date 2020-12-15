#!/usr/bin/python3.6
import ym
import subprocess

name = ym.xmlFileName

download = f'lftp sftp://domodedova:Hew3wruf@57.250.192.37 -e "cd CKIXML; mget {name}; quit"'
subprocess.call(download, shell=True)

move = f'mv /home/black/sftpscripts/{name} /home/black/sitadata'
subprocess.call(move, shell=True)

send = f'mpack -s "AUTO SCRIPT: don\'t reply to this message. {name}" ~/sitadata/{name} orkhangasanov@dme.ru'
subprocess.call(send, shell=True)
# send1 = f'mpack -s "AUTO SCRIPT: don\'t reply to this message. {name}" ~/sitadata/{name} andreytelegin@dme.ru'
# subprocess.call(send1, shell=True)

#

