'''
FORMATAÇÃO DE MÁSCARA

Assim como em outras linguagens, é possível utilizar identificadores para representar os tipos de dados armazenados nas variáveis que devem ser exibidas na tela.
O Python utiliza a formatação comum entre várias linguagens de desenvolvimento para as máscaras.
Exemplo na tabela abaixo de Máscara, tipo de Dados e Descrição:

%d ou %1     Int (inteiro)       Exibe um valor inteiro.
%f           Float ou double     Exibe um valor decimal.
%id          Long Int            Exibe um número inteiro longo.
%e ou %E     Float e double      Exibe um número exponencial (número científico)
%c           Char (caractere)    Exibe um caractere.
%o           Int                 Exibe um número inteiro em formato octal.
%x ou %X     Int                 Exibe um número inteiro no formato hexadecimal.
%s           Char                Exibe uma cadeira de caracteres (string).
%r           Boolean             Exibo True ou False (verdadeiro ou falso).

vide exemplos abaixo de aplicação:
'''

fruta = 'Laranja'
print(fruta)
print('Meu suco favorito é de ' + fruta)  # User, por padrão
print('Meu suco favorito é de...', fruta)
print('Suco de %s é o meu favorito' %fruta)


#Exercício: exiba a mensagem "Suco de laranja é meu favorito, amo laranja."
print('Suco de %s é o meu favorito, amo %s' %(fruta, fruta))
print('Suco de {} é meu favorito' .format(fruta))

cor1 = 'Azul'
cor2 = 'Vermelha'
cor3 = 'Preta'

print('Gosto do céu {}, a flor {} e para o carro prefiro a cor {}'.format(cor1, cor2, cor3))
print('Gosto do céu {0}, a flor {1} e para o carro prefiro a cor {0}'.format(cor1, cor2))

conta = 10/3
print(conta)

print('O valor da conta é %f' %conta)
print('O valor da conta é %i' %conta)
print('O valor da conta é {}'.format(conta))
print('O valor da conta é %.2f' %conta)
print('O valor da conta é {:.2f}'.format(conta))

