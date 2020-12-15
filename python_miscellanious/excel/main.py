


#lst = []

#with open(r'C:\OG\workspace\venv_projects\excel\users.csv', 'r', encoding='utf-8') as f:
#    for line in islice(f, 2, None):
#        stripped_line = line.strip('\n')
#        lst.append(stripped_line.split(','))


def users_migrate():
    from user_model.models import UserModel, UserRole
    from itertools import islice
    
    lst = []

    with open(r'C:\OG\workspace\venv_projects\excel\users.csv', 'r', encoding='utf-8') as f:
        for line in islice(f, 2, None):
            stripped_line = line.strip('\n')
            lst.append(stripped_line.split(','))
        
    for user_data in lst:
        user = UserModel()
        if user_data[3] == 'DIS-ADMIN':
            user.username = user_data[0]
            user.fullname = user_data[1]
            user.set_password(user_data[2].lower())
            user.role = UserRole.objects.get(title=user_data[3])
            user.is_staff = True
            user.is_admin = True
            user.is_superuser = True
            user.save()
        else:
            user.username = user_data[0]
            user.fullname = user_data[1]
            user.set_password(user_data[2].lower())
            user.role = UserRole.objects.get(title=user_data[3])
            user.is_staff = True
            user.save()
