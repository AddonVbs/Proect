import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
# print(Fore.MAGENTA + 'зеленый текст' + Back.MAGENTA)
# print(Back.YELLOW + 'на желтом фоне')
# print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
# print('обычный текст')
users = {
    "maksim": "2311",
    "yaroslav" : "1091"
}
print("Для входа нажмите - 1")
print("Для регистрации нажмите - 2")

inputLoginOrReg = input()

if inputLoginOrReg == "1":  # Вход в систему
    print("Введите логин:")
    login = input()
    print("Введите пароль:")
    password = input()
elif inputLoginOrReg == "2":  # Регистрация нового пользователя
    print("Введите новый логин:")
    new_login = input()

if login in users and users[login] == password:
    print(f"Добро пожаловать, {login}!")
else:
    print("Неверный логил или пароль!")

if new_login in users:
    print("Этот логин уже занят. Попробуйте другой.")
else:
    print("Введите новый пароль:")




