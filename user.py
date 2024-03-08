import store

def register_user(username, password):
    if not username or username == "":
        return False
    if not password or password == "":
        return False
    return store.create_user(username, password)

def login_user(username, password):
    user_details = store.get_user_details(username)
    if not user_details:
        return False
    
    return user_details.get("password") == password

    