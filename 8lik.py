# decimal_to_octal.py

def decimal_to_octal(decimal_number):
    # 10-likdan 8-lik tizimga o'tkazish
    return oct(decimal_number)[2:]


# Foydalanuvchidan 10-lik sonni olish
decimal_number = int(input("10-lik sonni kiriting: "))
octal_number = decimal_to_octal(decimal_number)
print(f"{decimal_number} ning 8-lik tizimidagi ko'rinishi: {octal_number}")
