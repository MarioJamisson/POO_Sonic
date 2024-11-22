from personagem import Personagem

class Inimigo(Personagem):
  def __init__(self, nome: str, velocidade: int, energia: int, ataque: int):
    super().__init__(nome, velocidade, energia)
    self.__ataque = ataque
  
  def atacar(self):
    print(f"O inimigo esta atacando com a força: {self.__ataque}")