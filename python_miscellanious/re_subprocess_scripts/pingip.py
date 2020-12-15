#!/usr/bin/python3

import subprocess as sp

def ping_ip(ip_address):
    """
    Ping IP address and return tuple:
    On success:
        * True
        * command output (stdout)
    On failure:
        * False
        * error output (stderr)
    """
    reply = sp.run(
    ['ping', '-c', '3', '-n', ip_address],
    stdout=sp.PIPE,
    stderr=sp.PIPE
    )
    
    if reply.returncode == 0:
        return True, reply.stdout.decode('utf-8')
    else:
        return False, reply.stderr.decode('utf-8')

print(ping_ip('127.0.0.1'))
print(ping_ip('a'))
