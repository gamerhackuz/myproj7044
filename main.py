import random
import string

def parol_yarat(uzunlik):
    # Barcha mumkin bo'lgan belgilarni jamlash
    harflar = string.ascii_letters
    raqamlar = string.digits
    belgilar = string.punctuation
    
    barcha_belgilar = harflar + raqamlar + belgilar
    
    # Tasodifiy tanlab olingan belgilarni birlashtirish
    parol = ''.join(random.choice(barcha_belgilar) for _ in range(uzunlik))
    return parol

print("--- 🔐 Tasodifiy Parol Generatori ---")
try:
    uzunlik = int(input("Parol uzunligini kiriting (masalan, 12): "))
    if uzunlik < 4:
        print("Parol kamida 4 ta belgidan iborat bo'lishi tavsiya etiladi.")
    else:
        yangi_parol = parol_yarat(uzunlik)
        print(f"✅ Sizning yangi parolingiz: {yangi_parol}")
except ValueError:
    print("❌ Xatolik: Iltimos, faqat butun son kiriting.")
