import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

file_names = []
dir_names = []
un_name = []


def store_files_name(fname):
    file_names.append(fname)


def store_dir_name(dirname):
    dir_names.append(dirname)


def store_other_file_types(name):
    un_name.append(name)


sftp = pysftp.Connection('57.250.192.37', username='domodedova', password='Hew3wruf', cnopts=cnopts)
walk = sftp.walktree('/OpenRes_Data_External/psl/users/152/', store_files_name, store_dir_name, store_other_file_types)
# print(sftp.listdir('/OpenRes_Data_External/psl/users/152/CKIXML'))
print(sftp.pwd)

print(file_names, dir_names, un_name)

# sftp.close()
