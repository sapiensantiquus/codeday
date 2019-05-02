from werkzeug.security import safe_str_cmp
from cryptography.fernet import Fernet


class UserInternal(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


def encrypt(key,password):
    cipher_suite = Fernet(key)
    encrypted_pass = cipher_suite.encrypt(password.encode('utf-8'))
    return  encrypted_pass


def identity(payload):
    user_id = payload['identity']
    user = User.query \
    .filter(User.user_id == user_id) \
    .one_or_none()
    if user:
        return UserInternal(user.user_id,user.username,cipher_suite.decrypt(user.password).decode())

def create(user):
    password = self.__encrypt(user.password)
    user.password = password
    schema = UserSchema()
    new_user = schema.load(user, session=db.session).data

    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()
    return

def auth(u, p):
    user = User.query \
    .filter(User.username == u) \
    .one_or_none()

    if user:
        e_pass = user.password
        d_pass = cipher_suite.decrypt(e_pass)
        if safe_str_cmp(d_pass.decode(), p.encode('utf-8')):
            return UserInternal(user.user_id,user.username,cipher_suite.decrypt(user.password).decode())
    return
