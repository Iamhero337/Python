id = 'iamhero337'
pas = 'thebeast'


uname = input('Give the Username: ')
pword = input('Give the password: ')


if id == uname:
    if pas == pword:
        print('You are iamhero337.')
    else:
        print('You have given the wrong password.')
else:
    print('No user avail with this username.')
