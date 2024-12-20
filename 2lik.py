# decimal_to_binary.py

def decimal_to_binary(decimal_number):
    # 10-likdan 2-lik tizimga o'tkazish
    return bin(decimal_number)[2:]


# Foydalanuvchidan 10-lik sonni olish
decimal_number = int(input("10-lik sonni kiriting: "))
binary_number = decimal_to_binary(decimal_number)
print(f"{decimal_number} ning 2-lik tizimidagi ko'rinishi: {binary_number}")
