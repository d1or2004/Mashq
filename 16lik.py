def decimal_to_hexadecimal(decimal_number):
    # 10-likdan 16-lik tizimga o'tkazish
    return hex(decimal_number)[2:].upper()


# Foydalanuvchidan 10-lik sonni olish
decimal_number = int(input("10-lik sonni kiriting: "))
hexadecimal_number = decimal_to_hexadecimal(decimal_number)
print(f"{decimal_number} ning 16-lik tizimidagi ko'rinishi: {hexadecimal_number}")
