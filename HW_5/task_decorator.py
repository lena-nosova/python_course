import functools

login = (input("Введите логин: "))
admin_users = {"Петя": 'admin'}

def check_login(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        if login in admin_users:
            print(login, sum)
            value = func(*args, **kwargs)
        return value
    return wrapper_decorator

@check_login
def not_acsess():
    if login not in admin_users:
        print("Доступ запрещен")
    