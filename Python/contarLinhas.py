arquivo = input('informe o nome do arquivo: ')
try:
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        print(f'O arquivo tem {len(linhas)} linhas.')
except FileNotFoundError:
    print('Arquivo não encontrado')