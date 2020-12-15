from sftpwalk import FTPWalk
import ftplib
import paramiko

# connection = ftplib.FTP('57.250.192.37')

# connection.login(username='domodedova', password='Hew3wruf')


sftpURL = '57.250.192.37'
sftpUser = 'domodedova'
sftpPass = 'Hew3wruf'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

connection = ssh.connect(sftpURL, username=sftpUser, password=sftpPass)

ftpwalk = FTPWalk(connection)
for i in ftpwalk.walk():
    print(i)
