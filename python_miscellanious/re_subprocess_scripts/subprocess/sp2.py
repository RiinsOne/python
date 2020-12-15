#!/usr/bin/python3
import subprocess as sp

sudo_pass = 'SITdcs12'
command = 'systemctl is-active messages --quiet'.split()
some_cmd = 'systemctl status messages'.split()

cmd1 = sp.Popen(['echo', sudo_pass], stdout=sp.PIPE)
cmd2 = sp.Popen(['sudo', '-S'] + command, stdin=cmd1.stdout, stdout=sp.PIPE)


s1 = sp.run('sudo systemctl is-active messages --quiet', shell=True, stdout=sp.PIPE)

if not s1.returncode:
    print('DME Messages is running and active')
else:
    print('DME Messages service is stopped or failed, please check as soon as possible')

print('poll method', cmd2.poll())

print('wait method', cmd2.wait())

out, err = cmd2.communicate()
print(out)
print(err)
print(cmd2.returncode)


# cmd2.communicate()[0]
# print(cmd2.returncode)
