class Controle:
  def __init__(self, marca, altura, cor, tamanho, fabricado,ligar = False):
    self.marca = marca
    self.altura = altura
    self.cor = cor
    self.tamanho = tamanho
    self.fabricado = fabricado
    self.ligar = ligar

  def apresentar(self):
    print('Controle Funcioando')
    print(f'{self.marca}\n{self.cor}\n{self.tamanho}\n{self.fabricado}\n')

  def verificar(self):
    if self.ligar == False:
      print('Você precisa ligar a TV')
    else:
      print('A TV Já está ligada')

  def iniciar(self):
    self.ligar = True
    if self.ligar == True:
      print('TV Ligada')

  def volume(self,botao):
    if botao == "+":
      self.altura += 1
      print(f'Aumentou para o volume: {self.altura}')

    if botao == "-":
      self.altura -= 1
      print(f'Diminuiu para o volume: {self.altura}')

    while self.altura < 0:
      print('-'*30)
      print('Você diminuiu abaixo de 0\nExperimente aumentar o volume')
      break
    
  def mudar(self,canal):
    if canal == 2:
      print(f'Você digitou {canal}, e mudou para emissora: SBT')
    elif canal == 4:
      print(f'Você digitou {canal}, e mudou para emissora: RECORD')
    elif canal == 6:
      print(f'Você digitou {canal}, e mudou para emissora: REDETV')
    elif canal == 9:
      print(f'Você digitou {canal}, e mudou para emissora: BAND')
    elif canal == 11:
      print(f'Você digitou {canal}, e mudou para emissora: UNIVERSITÁRIA')
    elif canal == 13:
      print(f'Você digitou {canal}, e mudou para emissora: GLOBO')

    if canal != 2 and canal != 4 and canal != 6 and canal != 9 and canal != 11 and canal != 13:
      print(f'Você digitou {canal}, essa emissora NÃO EXISTE')

  def desligar(self):
    self.ligar = False
    if self.ligar == False:
      print('TV Desligada')
