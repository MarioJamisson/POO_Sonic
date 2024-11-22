class Personagem:
  def __init__(self, nome:"str", velocidade:int, energia:int):
    self.__nome = nome
    self.__velocidade = velocidade
    self.__energia = energia

  def status(self):
    print(f"Nome: {self.__nome}, Velocidade: {self.__velocidade}, Aneis: {self.__energia}")
  
  def correr(self):
    self.__energia -= 10
    print(f"O personagem {self.__nome} está correndo na velocidade: {self.__velocidade} km/h e com {self.__energia} aneis")

  def descansar(self):
    self.__energia += 20
    if self.__energia <= 100: 
      print(f"{self.__nome} está descansando") 
    else:
      print("Erro: ultrapassou o limite")