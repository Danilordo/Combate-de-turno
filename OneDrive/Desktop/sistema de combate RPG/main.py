
#variaveis dos personagens
class personagem:
  def __init__(
      self,
      nome,
      hp,
      mana,
      forca,
      defesa,
      resistencia_magica,
      inteligencia
      ):

    self.nome = nome
    self.hp = hp
    self.mana = mana
    self.forca = forca
    self.inteligencia = inteligencia
    self.defesa = defesa
    self.resistencia_magica = resistencia_magica


#personagens
guerreiro = personagem(
    "Brabo",
    250,  # hp
    30,   # mana
    40,   # força
    15,   # defesa
    10,   # resistência mágica
    5     # inteligência
)

mago = personagem(
    "Ronaldo",
    120,  # hp
    100,  # mana
    10,   # força
    8,    # defesa
    20,   # resistência mágica
    45    # inteligência
)

boss = personagem(
    "Dragonico",
    600,  # hp
    50,   # mana
    30,   # força
    20,   # defesa
    15,   # resistência mágica
    15    # inteligência
)



#funções de dano
import random

#ataque
def ataque(atacante, alvo):
  dano = atacante.forca - alvo.defesa

  if dano < 1:
    dano = 1

  alvo.hp -= dano
  print(f"{atacante.nome} causou {dano} de dano em {alvo.nome}")
  print(f"HP restante de {alvo.nome}: {alvo.hp}")

#ataque magico
def magia(atacante, alvo):
  dano = atacante.inteligencia - alvo.resistencia_magica

  if dano < 1:
    dano = 1

  alvo.hp -= dano

  print(f"{atacante.nome} causou {dano} de dano em {alvo.nome}")
  print(f"HP restante de {alvo.nome}: {alvo.hp}")


#menu
def menu(atacante, alvo):
  print("MENU")
  print("1 atacar")
  print("2 magia")
  print("3 item")

  acao = int(input("ESCOLHA UMA AÇÃO:"))

  if acao == 1:
    print("usou ataque")
    ataque(atacante, alvo)

  elif acao == 2:
    print("usou magia")
    magia(atacante, alvo)

  elif acao == 3:
    print("usou item")

#status de personagem antes da batalha
print(f"{guerreiro.nome} tem {guerreiro.hp} de vida")
print(f"{mago.hp} tem {mago.hp} de vida e {mago.mana} de mana")

#sistema de turno

personagens = [guerreiro, mago]

while boss.hp > 0:
    for personagem_ativo in personagens:
      if personagem_ativo.hp <= 0:
        continue
      
      menu(personagem_ativo, boss)

    print("TURNO DO BOSS")
    ataque(boss, personagens[0])

#fim da batalha
if boss.hp <= 0:
  print("VITORIA")
elif guerreiro.hp <= 0 and mago.hp <= 0:
  print("GAME OVER")