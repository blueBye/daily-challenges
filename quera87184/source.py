import functools
import re
from hashlib import sha256


class Site:
    def __init__(self, url_address):
        self.url = url_address
        self.register_users: list[Account] = []
        self.active_users: list[Account] = []

    def show_users(self):
        pass

    def register(self, user):
        if user in self.register_users:
            raise Exception("user already registered")
        self.register_users.append(user)
        return "register successful"

    def login(self, **kwargs):
        email: str | None = kwargs.get('email')
        username: str | None = kwargs.get('username')
        password: str | None = kwargs.get('password')

        user = None
        fdata = filter(lambda u: u.password == sha256(password.encode()).hexdigest(), self.register_users)

        if username:
            fdata = filter(lambda u: u.username == username, fdata)
        elif email:
            fdata = filter(lambda u: u.email == email, fdata)
        user = next(iter(list(fdata)), None)
        
        if user:
            if user in self.active_users:
                return "user already logged in"
            self.active_users.append(user)
            return "login successful"
        return "invalid login"

    def logout(self, user):
        if user in self.active_users:
            self.active_users.remove(user)
            return "logout successful"
        return "user is not logged in"

    def __repr__(self):
        return "Site url:%s\nregister_users:%s\nactive_users:%s" % (self.url, self.register_users, self.active_users)

    def __str__(self):
        return self.url


class Account:
    def __init__(self, username, password, user_id, phone, email):
        self.username = self.username_validation(username)
        self.password = self.password_validation(password)
        self.user_id = self.id_validation(user_id)
        self.phone = self.phone_validation(phone)
        self.email = self.email_validation(email)

    def set_new_password(self, password):
        if self.password_validation(password):
            self.password = self.password_validation(password)
            return True
        return False

    def username_validation(self, username):
        if re.match('^[a-zA-Z]+_[a-zA-Z]+$', username):
            return username
        raise Exception("invalid username")

    def password_validation(self, password: str):
        if len(password) >= 8 and \
            re.search('[0-9]', password) and \
            re.search('[a-z]', password) and \
            re.search('[A-Z]', password):
            return sha256(password.encode()).hexdigest()
        raise Exception("invalid password")

    def id_validation(self, id):
        if len(id) == 10:
            s = sum([int(id[i])*(10-i) for i in range(9)])
            d = s % 11
            if (d < 2) and (int(id[-1]) == d):
                return id
            if (d >= 2) and (int(id[-1]) == 11 - d):
                return id
        raise Exception("invalid code melli")

    def phone_validation(self, phone):
        if re.match("^(\+989|09)[0-9]{9}$", phone):
            return f"09{phone[-9:]}"
        raise Exception("invalid phone number") 

    def email_validation(self, email):
        if re.match("^[A-Za-z0-9._-]+@[A-Za-z0-9._-]+\.[a-zA-Z]{2,5}$", email):
            return email
        raise Exception("invalid email")

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username


def show_welcome(func):
    @functools.wraps(func)
    def wrapper_decorator(user: Account):
        first_name, last_name = user.username.split('_')
        username = f'{first_name.capitalize()} {last_name.capitalize()}'
        if len(username) > 15:
            username = f"{username[:15]}..."
        return func(username)
    return wrapper_decorator

def verify_change_password(func):
    @functools.wraps(func)
    def wrapper_decorator(user: Account, old_pass: str, new_pass: str):
        if user.password == sha256(old_pass.encode()).hexdigest():
            if user.set_new_password(new_pass):
                return func(user, old_pass, new_pass)
    return wrapper_decorator

@show_welcome
def welcome(user):
    return ("welcome to our site %s" % user)

@verify_change_password
def change_password(user, old_pass, new_pass):
    return ("your password is changed successfully.")
