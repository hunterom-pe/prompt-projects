# Sample Input V1 (Raw Text)

Dev Python code example:

def filter_active_users(users):
    active = []    
    for user in users:
        if user['is_active'] and user['last_login'] is not None:
            active.append(user)
    return active