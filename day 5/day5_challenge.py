import random

letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 
    "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-" ] 


print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n\t >>> "))
n_numbers = int(input("How many numbers your like? \n\t >>> "))
n_symbols = int(input("How many symbols would you like?\n\t >>> "))

password = ""
for i in range(n_letters):
    i = random.randint(0,len(letters)-1)
    password += letters[i]

for i in range(n_numbers):
    i = random.randint(0,len(numbers)-1)
    password += numbers[i]

for i in range(n_symbols):
    i = random.randint(0,len(symbols)-1)
    password += symbols[i]

# SENHA NÃO EMBARALHADA
print(password)

password_list = list(password)
# Embaralhar a lista
random.shuffle(password_list)
# Juntar de volta em uma string
password_shuffled = ""
for i in password_list:
    password_shuffled += i
    
print("Senha embaralhada:", password_shuffled)

# ESSE CODIGO COMEÇA COM UMA STRING VAZIA COMEÇA UM LOOP PARA CONCATENAR AS LETRAS EM SEGUIDA OS NUMEROS E LOGO APOS OS SIMBOLOS 
# AGORA TEMOS UMA SENHA COM A SEQUENCIA DE N(LETARAS)+N(NUMEROS)+N(SIMBOLOS)
#  HORA DE EMBARALHAR 
#  TRANSFORMEI EM LISTA list(password)
#  EMBARALHO A LISTA UTILIZANDO O .shuffle
#  COM O PASSWORD EMBARALHADO É PRECISO TRANSFORMA EM STRING
#  UTILIZO O METODO .join(password_list) PARA TRANSFORMAR EM STRING
#  E DOU PRINT
#  FIM!!

# OUTRO METODO POREM MAIS AVANÇADO QUE EU VI
# password_shuffled = ''.join(random.sample(password, len(password)))
# print(password_shuffled)