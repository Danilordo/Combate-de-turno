# ⚔️ Combate de Turno

Um projeto de **combate por turnos desenvolvido em Python**, criado para praticar programação, lógica de programação e conceitos de Programação Orientada a Objetos.

O projeto simula uma batalha entre personagens com diferentes atributos, permitindo realizar ataques físicos e mágicos durante os turnos.

## 🎮 Sobre o projeto

O sistema possui personagens com atributos próprios, como:

* ❤️ HP
* 🔮 Mana
* ⚔️ Força
* 🛡️ Defesa
* ✨ Resistência Mágica
* 🧠 Inteligência

Durante o combate, cada personagem pode escolher uma ação através de um menu. Atualmente, estão disponíveis ataques físicos, magia e uma opção de item em desenvolvimento.

O combate continua enquanto o chefe possuir pontos de vida.

## 🧙 Personagens

Atualmente o projeto possui:

| Personagem |  HP | Mana | Força | Defesa | Resistência Mágica | Inteligência |
| ---------- | --: | ---: | ----: | -----: | -----------------: | -----------: |
| Brabo      | 250 |   30 |    40 |     15 |                 10 |            5 |
| Ronaldo    | 120 |  100 |    10 |      8 |                 20 |           45 |
| Dragonico  | 600 |   50 |    30 |     20 |                 15 |           15 |

## ⚔️ Sistema de combate

O dano dos ataques é calculado a partir dos atributos dos personagens.

### Ataque físico

O dano é calculado utilizando:

```text
Força do atacante - Defesa do alvo
```

O dano mínimo é `1`.

### Ataque mágico

O dano é calculado utilizando:

```text
Inteligência do atacante - Resistência Mágica do alvo
```

O dano mínimo também é `1`.

## 🧠 Conceitos praticados

Este projeto foi desenvolvido com foco no aprendizado e prática de:

* Python
* Classes e objetos
* Programação Orientada a Objetos
* Funções
* Estruturas condicionais
* Laços de repetição
* Listas
* Manipulação de objetos
* Entrada de dados pelo usuário
* Geração de números aleatórios
* Lógica de combate por turnos

## 🚧 Próximos passos

O projeto ainda está em desenvolvimento. Algumas ideias para futuras versões:

* [ ] Sistema de itens
* [ ] Mais habilidades e magias
* [ ] Sistema de iniciativa
* [ ] Diferentes tipos de inimigos
* [ ] Sistema de experiência e níveis
* [ ] Inventário
* [ ] Status e efeitos temporários
* [ ] Melhor organização do código em diferentes módulos
* [ ] Implementação de estruturas de dados para gerenciamento dos turnos
* [ ] Interface gráfica

## ▶️ Como executar

### Pré-requisitos

* Python 3.x

### Executando o projeto

Clone o repositório:

```bash
git clone https://github.com/Danilordo/Combate-de-turno.git
```

Entre na pasta:

```bash
cd Combate-de-turno
```

Execute:

```bash
python main.py
```

## 📚 Objetivo

Este projeto faz parte da minha prática de programação e tem como objetivo transformar conceitos estudados em projetos funcionais, evoluindo gradualmente a complexidade do código.

---

**Desenvolvido por Danilo**
🐍 Python | 🎮 Game Logic | 💻 Programação
