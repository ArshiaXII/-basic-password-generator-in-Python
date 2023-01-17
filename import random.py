import random
import string

def generate_password(length, special_characters=False):
    password = ""
    allowed_characters = string.ascii_letters + string.digits
    if special_characters:
        allowed_characters += string.punctuation
    for i in range(length):
        password += random.choice(allowed_characters)
    return password

length = int(input("şifrenin uzunluğunu gir: "))
special_characters = input("özel karakter içersin mı? (y/n): ") == 'y'
password = generate_password(length, special_characters)
print("oluşturulan şifre: ", password)
