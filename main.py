from random import choice
import string
import clipboard

use = string.ascii_letters+string.digits+string.punctuation
#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

tamanho = 12 # Irá gerá uma senha de 12 dígtos
senha = ''

for i in range(tamanho):
  senha += choice(use)

print(f"Senha gerada: {senha}, copiada direto para seu clipboard!")

clipboard.copy(senha)

