from aula7_televisao import  Televisao
from  aula7_calculadora1 import  Calculadora
from aula8_contador_letras import  contador_letras

if __name__ == '__main__':
    Televisao = Televisao()
    print(Televisao.ligada)
    Televisao.power()
    print(Televisao.ligada)
    Calculadora = Calculadora(5 , 10)
    print(Calculadora.soma())
    lista = ['cachorro','elefante']
    total_letras = contador_letras(lista)
    print('Total de letras por palavras de lista: {}'.format(total_letras))