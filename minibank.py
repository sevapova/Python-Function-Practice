from typing import Union

# Global variables
name: Union[str, None] = None
balance: Union[float, None] = None

def open_account() -> None:
    """Yangi accaunt yaratish.

Foydalanuvchidan ism so'raladi va 'balance' 0.0 qilib boshlanadi.

 Scope:
        - Global: 'name' va 'balance' o'zgaruvchilari global tarzda yangilanadi.
    """
    global name, balance
    name = input("name = ")
    balance = 0.0

def check_account() -> bool:
    """ Hisob ochilgan yoki ochilmaganligini tekshiradi..

    Returns:
        bool: Agar 'name' va 'balance' mavjud bo'lsa (ya'ni 'None' bo'lmasa), 'True', aks holda 'False'.
   
    Scope:
        - Global: 'name', 'balance' ni faqat o'qiydi (read-only).
    """
    return name is not None and balance is not None

def deposit() -> None:
    """Pul qo'shish funksiyasi.

    Foydalanuvchidan miqdor so'raladi va 'balance' ga qo'shiladi.

    Raises:
        ValueError: Agar kiritilgan qiymat son (float) emas bo'lsa.

    Scope:
        - Global: 'balance' ni o'zgartiradi (write).
        - Local: 'amount' faqat shu funksiya doirasida ishlatiladi.
    """
    global balance
    amount = float(input("Qo'shiladigan summani kiriting: "))
    balance += amount

def withdraw() -> None:
    """Pul yechish funksiyasi.

    Foydalanuvchidan yechiladigan miqdor so'raladi va 'balance' dan ayiriladi.

    Raises:
        ValueError: Agar noto'g'ri raqam kiritilsa.
        RuntimeError: Agar balans yetarli bo'lmasa.

    Scope:
        - Global: 'balance' ni o'zgartiradi (write).
        - Local: 'amount' faqat funksiya doirasida mavjud.
    """
    global balance
    amount = float(input("Yechiladigan summani kiriting: "))
    balance -= amount

def check_balance() -> None:
    """Balansni ko'rsatish funksiyasi.

    Hisobdagi mavjud mablag'ni ekranga chiqaradi.

    Scope:
        - Global: 'balance' ni o'qiydi (read)."""
    print(f"Hozirgi balans: {balance} so'm")

def main() -> None:
    """Asosiy dastur funksiyasi (menu bilan).

    Foydalanuvchiga quyidagi amallarni bajarish imkonini beradi:
    - Hisob yaratish
    - Balansni ko'rish
    - Pul qo'shish
    - Pul yechish
    - Chiqish

    Scope:
        - Global: 'name', 'balance' dan foydalanadi.
        - Local: 'tanlov' — foydalanuvchi tanlovi uchun faqat bu yerda mavjud.
    """
    while True:
        print("\n=== ATM Menyusi ===")
        print("0 - Account yaratish")
        print("1 - Balansni ko'rish")
        print("2 - Pul qo'shish (deposit)")
        print("3 - Pul yechish (withdraw)")
        print("4 - Chiqish")

        tanlov = input("Amalni tanlang (0-4): ")

        if tanlov == "0":
            open_account()
        elif tanlov == "1":
            if check_account():
                check_balance()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "2":
            if check_account():
                deposit()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "3":
            if check_account():
                withdraw()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "4":
            print("Dasturdan chiqildi. Xayr!")
            break
        else:
            print("Noto'g'ri tanlov! Iltimos, qaytadan urinib ko'ring.")

# Dastur ishga tushiriladi
main()

