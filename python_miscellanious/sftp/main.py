import paramiko

host = '57.250.192.37'
user = 'domodedova'
secret = 'Hew3wruf'
port = 22

transport = paramiko.Transport((host, port))
transport.connect(username=user, password=secret)
sftp = paramiko.SFTPClient.from_transport(transport)

print(sftp.stat('/CKIXML/*'))
# remotepath = '/CKIXML/*'
# localpath = 'C:\OG\Misc\Downloads'

# sftp.get(remotepath, localpath)
# sftp.put(localpath, remotepath)

# sftp.close()
# transport.close()
