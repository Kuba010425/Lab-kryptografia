from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def szyfrowanie(plik):
    print ("\n ------------------------------------")
    hasło = input("podaj hasło do zaszyfrowania pliku: ")
    key = hashlib.sha256(hasło.encode()).digest() #hasło zostaje zhaszowane aby miało 32 bajty długości co umozliwia sha256
    iv = hashlib.md5(hasło.encode()).digest() #hasło zostaje zhaszowane aby miało 16 bajtów długości co umożliwia md5
    with open(plik, 'rb') as f: #otwieramy plik binarnie
        dane = f.read()
    dane_padded=pad(dane, AES.block_size) #ponieważ AES czyfruje w blokach po 16 bajtów dodajemy do tekstu brakującą ilość którą pozniej mozna usunąć
    szyfr = AES.new(key, AES.MODE_CBC, iv) #tworzenie szyfru z wykorzystaniem klucza oraz iv(aby nasze dane były dobrze zaszyfrowane)
    zaszyfrowane= szyfr.encrypt(dane_padded) #szyfrowanie pliku
    with open(plik, 'wb') as f: #wprowadzenie do pliku zaszyfrowanego tekstu
        f.write(zaszyfrowane)
    print("pomyślnie zaszyfrowano!")

def odszyfrowanie (plik):
    print ("\n ------------------------------------")
    hasło = input("podaj klucz do odszyfrowania pliku: ")
    key = hashlib.sha256(hasło.encode()).digest() #haszowanie sha256
    iv = hashlib.md5(hasło.encode()).digest() #haszowanie md5
    with open(plik, 'rb') as f: #otwieranie binarne pliku
        zaszyfrowane = f.read()
    szyfr = AES.new(key, AES.MODE_CBC, iv)  #tworzenie Szyfru
    dane = szyfr.decrypt(zaszyfrowane) #odszyfrowywanie pliku utworzonym szfrem
    dane = unpad(dane, AES.block_size) #usuniecie dodanych bajtów tekstu
    with open(plik, 'wb') as f: #zapisanie zmian do pliku tekstowego
        f.write(dane)
    print("pomyślnie odszyfrowano!")


plik = input("\n podaj ścieżke do pliku który chcesz zaszyfrować lub odzsyfrować za pomocą AES-256: ")
print("\n")

typ=True

while (typ): #pętla służy temu aby użytkownik wprowadził poprawną opcję albo zaszyfrowania albo odszyfrowania
    print("------------------------------------------------------------------------")
    t = input("jezeli chcesz zaszyfrowac wprowadź 's' jeśli odszyfrować wprowadź 'o': ")
    if (t!="s" and t!= "o"):
        print("wybrano niepoprawną opcję")
        print("\n")
    else:
        typ=False
if (t=="s"): #jeżeli uzytkownik wybierze s to szyfrujemy a jesli o to odszyfrujemy
    szyfrowanie(plik) 
else:
    odszyfrowanie(plik)

    


    


