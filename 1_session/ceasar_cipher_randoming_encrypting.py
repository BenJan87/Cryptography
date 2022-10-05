from string import ascii_lowercase as alphabet
from collections import Counter as ctr

alphabet = list(alphabet)
alphabet_size = len(alphabet)

plaintext = "tobeornottobethatisthequestionwhethertisnoblerinthemindtosuffertheslingsandarrowsofoutrageousfortuneortotakearmsagainstaseaoftroublesandbyopposingendthem"
key = "klucz"
ciphertext = ""

key_length = len(key)

for i in range(len(plaintext)):
  tmp_key_index = alphabet.index(key[i % key_length])
  ciphertext += alphabet[(alphabet.index(plaintext[i]) + tmp_key_index) % alphabet_size]

print("zaszyfrowana wiadomosc:", ciphertext)
print("Rozkład: ", ctr(ciphertext).most_common())