import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from personagem import Personagem
from inimigo import Inimigo

personagem1 = Personagem(nome="Sonic", velocidade=100, energia=80)
inimigo1 = Inimigo(nome="Dr. Eggman", velocidade=20, energia=50, ataque=30)

personagem1.status()
personagem1.correr()
personagem1.correr()
personagem1.descansar()

inimigo1.status()
inimigo1.atacar()
inimigo1.descansar()


