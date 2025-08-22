import hashlib  # Gerar o hash da senha testada e comparar com o alvo
import itertools  # Gerar todas as combinações possíveis de caracteres
import string  # Fornecer listas prontas de letras e numeros para o charset
import time  # Medir o tempo total de execução da quebra

# Entrada has do md5
hash_alvo = input("Digite o hash md5 a ser quebrado: ").strip()

#Tratamento de arquivo externo
try:
    with open(hash_alvo, 'r') as arq:
        hash_alvo = arq.read().strip()
except FileExistsError:
    print('Arquivo não encontrado. ')
    exit()

#hash_alvo = 'c6663e689b7d1495526d8c7403ccc67f'

#Charset reduzido para os caracteres a-z 0-9
#caracteres = string.ascii_lowercase + string.digits
#Charset de caracteres wordlist
caracteres = '0123456789qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM[ç~].;/\|'
#Estimativa com o tamanho 4 33,8 milhões de tentativas em 3 dias e 22 horas

# Definir o conjunto de caracteres a testar a-z 0-9
#caracteres = string.ascii_lowercase = string.digits

# Define o tamanho máximo da senha a testar
tamanho_maximo = 6

#Contador para calcular o nível de dificuldade para quebrar a hash
tentativas = 0
# f na frente do string é um recurso chamado f-string para interpolação de variáveis dentro de strings
print(f"Iniciando força bruta para o has: {hash_alvo}")
print(f"Charset: {caracteres} | Tamanho máximo: {tamanho_maximo}")

inicio = time.time()
encontrado = False

# Loop sobre tamanhos de 1 até o máximo definido
for tamanho in range(1, tamanho_maximo + 1):
    print(f"Tentando combinações com {tamanho} caracteres.")

# Gera todas as combinações possivéis com charset e o tamanho atual
#intertools.product gera todas as combinações de caracteres e tamanho
    for tentativa in itertools.product(caracteres, repeat=tamanho):
#''.join para as tentativas de encontrar os dígitos
        palavra = ''.join(tentativa)
#hashlib.md5 .hexdigest gera o hash md5 da senha testada .encode converte a string para bytes
        hash_teste = hashlib.md5(palavra.encode()).hexdigest()
        tentativas += 1 #incremento das tentativas

# Se o hash da tentativa for igual ao hash alvo, senha foi descoberta
        if hash_teste == hash_alvo:
            print(f"Senha encontrada: {palavra}")
            print(f"Tentativas: {tentativas}")
            encontrado = True
            break

#Sai do loop principal ao encontrar a senha
        if encontrado:
            break

#Sai do loop das tentativas de força bruta quando não encontrada e exibe a mensagem
        if not encontrado:
            print("Senha não encontrada. Tente aumentar o tamanho máximo ou o charset.")
#Fim da execução e tempo total
            fim = time.time()
            print(f"Tempo total de execução: {fim - inicio:.2f} segundos")

