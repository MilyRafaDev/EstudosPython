import random
n1 = random.randint(1,99)
n2 = random.randint(1,99)

p9 = n1 + n2

while True:  # Loop infinito que só termina com 'break'
    res = int(input('Resolva a seguinte adição: {} + {} = '.format(n1, n2)))
    if res == p9:
        print('Parabéns! Você conseguiu!')
        break  # Sai do loop quando a resposta está correta
    else:
        print('Errado! Vamos tentar novamente?')
