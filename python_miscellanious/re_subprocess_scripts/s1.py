#!/usr/bin/python3

import os
#print(os.ctermid())
#print(os.environ['HOME'])
#print(os.getenv('HOME'))

home_dir = os.environ['HOME']
#print('home dir is:', home_dir)
#new_dir = '/home/admdcs/messages'
#os.chdir(new_dir)
#print('current dir is:', os.getcwd())

#print(os.get_exec_path())
#print(os.getgroups())
#print(os.getlogin())

#print(os.getppid())

#print(os.uname())

#print(os.getcwdb())

#os.system('ls -l')

print(os.times())
