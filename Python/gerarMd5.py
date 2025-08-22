import hashlib #Biblioteca para calcular funções de hash md5, sha1, sha256.

arquivo = input('Digite o nome do arquivo: ')

#Tratamento de erro pra evitar que o programa quebre se o arquivo não existir. Bloco e código e a execeção.
try: 
#With garante que o arquivo em modo binário será fechado corretamente após o uso
    with open(arquivo, 'rb') as f:
#Cria um objeto hash usando o algoritmo md5
        md5 = hashlib.md5()
#Lê o arquivo em blocos de 4096 bytes para arquivos grandes, evitando o consumo excessivo de memória
        for chunk in iter(lambda: f.read(4096), b""):
#Adiciona o conteúdo do bloco ao hash
            md5.update(chunk)
#Exibe o hash md5 em formato hexadecimal
            print(f"MD5: {md5.hexdigest()}")
#Fechamento do bloco try
except FileExistsError:
    print('Arquivo não encontrado.')
