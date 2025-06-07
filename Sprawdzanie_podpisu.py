from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

plik = input("Podaj nazwę pliku do weryfikacji podpisu: ")
with open(plik, "rb") as f:
    dane = f.read()
with open(plik , "rb") as f:
    podpis = f.read()
with open("klucz_publiczny.txt", "rb") as f:
    pub_pem = f.read()
klucz_publiczny = serialization.load_pem_public_key(pub_pem)
try:
    klucz_publiczny.verify(
        podpis,
        dane,
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    print("Podpis jest prawidłowy. Dane nie zostały zmienione.")
except Exception as e:
    print("Weryfikacja podpisu nie powiodła się! Dane mogły zostać zmienione lub podpis jest nieprawidłowy.")