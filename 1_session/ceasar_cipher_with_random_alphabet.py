import numpy as np
from string import ascii_lowercase as alphabet

plaintext = "Zorro fly zealotry zipper"
joined_text = ""
key = 15
alphabet_size = 26
alphabet = list(alphabet)

for word in plaintext.lower().split():
  for char in word:
    joined_text += char

char_list = [el for el in joined_text]

random_alphabet = list(np.random.permutation(alphabet))

result_text = ""

for char in char_list:
  result_text = result_text + random_alphabet[(random_alphabet.index(char) + key) % alphabet_size] 
print("Szyfrogram: ",  result_text, "(spacje usunięte)")
