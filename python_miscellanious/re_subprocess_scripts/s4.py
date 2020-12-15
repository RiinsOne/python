import subprocess

out = sp.run('df -h | grep /dev/sd', shell=True, stdout=sp.PIPE)
out.stdout.decode('utf-8')
