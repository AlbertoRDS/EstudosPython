class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power( self ):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal( self ):
      if self.ligada:
          self.canal += 1


    def duminui_canal( self ):
        if self.ligada :
            self.canal -= 1

if __name__ == '__main__':
    Televisao = Televisao()
    print('Televisao esta ligada: {}'.format(Televisao.ligada))
    Televisao.power()
    print('Televisao esta ligada: {}'.format(Televisao.ligada))
    Televisao.power()
    print('Televisao esta ligada: {}'.format(Televisao.ligada))
    print('Canal: {}'.format(Televisao.canal))
    Televisao.power()
    print('Televisao esta ligada: {}'.format(Televisao.ligada))
    Televisao.aumenta_canal()
    Televisao.aumenta_canal()
    print('Canal: {}'.format(Televisao.canal))
    Televisao.duminui_canal()
    print('Canal: {}'.format(Televisao.canal))