import pytest
import subprocess
from hr import hr_user_manag

#Encrypted version of password
password = '$6$HXdlMJqcV8LZ1DIF$LCXVxmaI/ySqNtLI6b64LszjM0V5AfD.ABaUcf4j9aJWse2t3Jr2AoB1zZxUfCr8SOG0XiMODVj2ajcQbZ4H4/'

user_dict = {
 'name': 'kevin',
 'groups': ['wheel', 'dev'],
 'password': password
              }

def test_users_add(mocker):
    """
    Given a user dictionary. 'hr_user_manag.add(...)' should
    utilize 'useradd' to create a user with the password
    and groups
    """

    mocker.patch('subprocess.call')
    hr_users_manag.add(user_dict)
    subprocess.call.assert_called_with(['useradd',
                                        '-p',
                                        password,
                                        '-G',
                                        'wheel, dev',
                                        'kevin',
                                        ])
def test_users_remove(mocker):
    """
    Given a user dictionary. 'hr_user_manag.remove_user(...)' should
    utilize 'userdel' to remove the user from the system
    """
    mocker.patch('subprocess.call')
    hr_users_manag.remove_user(user_dict)
    subprocess.call.assert_called_with (['userdel',
                                        '-r',
                                        'kevin',
                                        ])

def test_user_update(mocker):
    """
    Given a user dictionary. 'hr_user_manag.update_user(...) should
    utilize 'usermod' to update the user information
    """
    mocker.patch('subprocess.call')
    hr_users_manag.update_user(user_dict)
    subprocess.call.assert_called_with(['usermod',
                                        '-p',
                                        password,
                                        '-G',
                                        'wheel, dev',
                                        'kevin',
                                        ])
def test_user_sync(mocker):
    """
    Given a list of user dictionaries, 'hr_user_manag.sync(...)
    create missing users, remove extra  non-system users, and update
    existing users. Alist of existing usernames can be passed in or
    default users will be used
    """
    existing_user_names = ['kevin','bob']
    users_info = [user_dict,
                  {
                   'name': 'jose',
                 'groups': ['wheel'],
               'password': password
                 }]

    mocker.patch('subprocess.call')
     hr_users_manag.sync(user_info, existing_user_names)
    subprocess.call.assert_has_calls([
        mocker.call(['usermod',
                    '-p',
                    password,
                    '-G',
                    'wheel,dev',
                    'kevin',
                    ]),
        mocker.call([
            'useradd',
            '-p',
            password,
            '-G',
            'wheel',
            'jose',
            ]),
        mocker.call(['userdel',
                    '-r',
                    'bob',
                    ]),
        ])



