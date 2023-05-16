from random import randint
from time import sleep

def jogarNovamente():
  rsp = str(input('\nDeseja jogar novamente? (s/n)> '))
  if rsp.lower() == 'n':
    print('\nFoi um prazer jogar com você, {}. Até breve! 😉'.format(nome.capitalize()))
    return False
  else:
    print('\nOBA! Vamos mais uma! 🤩')
    return True

def placar():
  print('\n------ PLACAR -------')
  print('Máquina: {} ponto(s)'.format(ptsPC))
  print('{}: {} ponto(s)'.format(nome.capitalize(), ptsPlayer))
  print('---------------------')

ptsPC = 0
ptsPlayer = 0

executando = True

nome = str(input('Seja bem-vindo(a) ao nosso jogo de adivinhação! Vamos brincar? 😄\n\nMas antes diga-me qual o seu nome > '))
print()

print('-='*40)
print('\nOlá, {}! Seja bem-vindo(a)! 🫡\n\nEscolhi um número entre 0 e 10. Será que você é capaz de adivinhar qual foi? 😜\n'.format(nome.capitalize()))
print('-='*40)

while executando:
  pc = randint(0, 10)
  player = int(input('\nMe diga: que número você acha que eu escolhi? '))

  print('\nEntão você acha que é {}? 🤔'.format(player))
  sleep(3)
  
  print('\nVamos ver... ⏳')
  sleep(3)

  if player == pc:
    print('\nPARABÉNS! 🥳 Você me venceu. Não fui o melhor dessa vez. 🫤')
    ptsPlayer += 1
    placar()
  else:
    print('\nERRADO! VENCI VOCÊ! 😎 O número que escolhi foi {} e não {}. Quem sabe na próxima. 🤷'.format(pc, player))
    ptsPC += 1
    placar()

  executando = jogarNovamente()
