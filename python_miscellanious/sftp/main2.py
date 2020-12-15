import paramiko

sftpURL = '57.250.192.37'
sftpUser = 'domodedova'
sftpPass = 'Hew3wruf'

ssh = paramiko.SSHClient()
# automatically add keys without requiring human intervention
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(sftpURL, username=sftpUser, password=sftpPass)

sftp = ssh.open_sftp()
files = sftp.listdir('/OpenRes_Data_External/psl/users/152/CKIXML')
print(files)

# remotepath = '/OpenRes_Data_External/psl/users/152/CKIXML/15204JUN19CKP.XML.gz.enc'
# localpath = 'C:\\OG\\Misc\\Downloads\\15204JUN19CKP.XML.gz.enc'

# sftp.get(remotepath, localpath)
sftp.close()
ssh.close()

