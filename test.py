from decouple import config


password = config("PASSWORD")
pin = config("PIN")
print(password)
print(pin)


