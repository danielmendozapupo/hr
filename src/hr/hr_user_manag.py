#!/usr/bin/env python3.6

import sys
import subprocess
import pwd


def add(user_info):
    print(f"Adding a new user '{user_info['name']}'")
    try:
        subprocess.call(['useradd',
                    '-p',
                    user_info['password'],
                    '-G',
                    _groups_str(user_info),
                    user_info['name'],
                    ])
    except:
        print(f"Failed to add user '{user_info['name']}'")
        sys.exit(1)

def remove_user(user_info):
    print(f"Removing user '{user_info['name']}'")

    try:
        subprocess.call(['userdel',
                        '-r',
                        user_info['name']
                        ])
    except:
        print(f"Failed to remove the user '{user_info['name']}'")
        sys.exit(1)

def update_user(user_info):
    print(f"Updating user '{user_info['name']}'")
    try:
        subprocess.call(['usermod',
                        '-p',
                        user_info['password'],
                        '-G',
                        _groups_str(user_info),
                        user_info['name'],
                        ])
    except:
        print(f"Failed to update the user '{user_info['name']}'")
        sys.exit(1)

def sync(users, existing_user_names=None):
    existing_user_names = (existing_user_names or _user_names())
    user_names = [user['name'] for user in users]
    for user in users:
        if user['name'] not in existing_user_names:
            add(user)
        elif user['name'] in existing_user_names:
            update_user(user)
    for user_name in existing_user_names:
        if not user_name in user_names:
            remove({'name': user_name})

def _groups_str(user_info):
    return '.'.join(user_info['groups'] or [])

def _user_names():
    return [user.pw_name for user in pwd.getwall()
            if user.pw_uid >= 1000 and 'home' in user.pw_dir]
