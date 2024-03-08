import store

def register_user(username, password):
    if not username or username == "":
        return False
    if not password or password == "":
        return False
    return store.create_user(username, password)

    