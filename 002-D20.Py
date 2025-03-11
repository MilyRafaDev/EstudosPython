import random
print('______________________________________________')
aposta = int(input('Adivinhe o resultado do D20: '))
num_aleatorio = random.randint(1,20) #O número será sorteado entre 1 e 20
while aposta != num_aleatorio: #O programa só para quando o usuario acertar o numero
       print('Errado! Tente Novamente.'.format(num_aleatorio))
       aposta = int(input('Adivinhe o resultado do D20: '))
if aposta == num_aleatorio:
    print('Parabéns! Você acertou.')
