# Quebra de hash = hash cracking
import hashlib

arquivo_hash = input('Digite o nome do arquivo que contém o hash md5: ')

try:
    with open(arquivo_hash, 'r') as arq:
        hash_alvo = arq.read().strip()
except FileExistsError:
    print('Arquivo não encontrado. ')
    exit()

# Lista de possíveis combinações (dicionário)
wordlist = ['123', 'admin', 'senha', 'root',
            'teste', 'abc', '123456', 'senha123']

print(f'Hash alvo: {hash_alvo}')
encontrado = False

# Buscar cada palavra da lista
for palavra in wordlist:
    hash_palavra = hashlib.md5(palavra.encode()).hexdigest()
    if hash_palavra == hash_alvo:
        print(f'Senha encontrada: {palavra}')
        encontrado = True
        break

if not encontrado:
    print('Senha não encontrada na wordlist.')
