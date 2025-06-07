from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

plik = input("Podaj nazwę pliku do podpisania: ")

with open(plik, "rb") as f:
    dane = f.read()

klucz_prywatny = rsa.generate_private_key(public_exponent=65537, key_size=2048) #tworzenie klucza prywatnego o długości 2048 bitów 
klucz_publiczny = klucz_prywatny.public_key() #tworzenie klucza publicznego w oparciu o klucz prywatny

prywatny = klucz_prywatny.private_bytes( #zmiana klucza na ciąg bajtów
    serialization.Encoding.PEM, #określenie formatu klucza jako ciąg znaków
    serialization.PrivateFormat.TraditionalOpenSSL, #określenie struktury wewnętrznej pliku
    serialization.NoEncryption() #przechowywyanie klucza bez hasła (nie jest to bezpieczne )
).decode() #konwertowanie bitów na znaki

with open("klucz_prywatny.txt", "w") as f:
    f.write(prywatny)

publiczny = klucz_publiczny.public_bytes( #zmiana klucza na ciąg bajtów
    serialization.Encoding.PEM, #zakodowanie w formacie Pem jako ciąg znaków
    serialization.PublicFormat.SubjectPublicKeyInfo #określenie standardowego formatu dla kluczy publicznych
).decode() #konwertowanie bitów na znaki

with open("klucz_publiczny.txt", "w") as f:
    f.write(publiczny)

podpis = klucz_prywatny.sign(dane, padding.PKCS1v15(), hashes.SHA256()) #tworzenie podpisu w pliku

with open(plik + ".sig", "wb") as f: #zapisanie podpisu
    f.write(podpis)

print("Plik został podpisany!")