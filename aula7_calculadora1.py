class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    Calculadora = Calculadora(10, 2)
    print(Calculadora.valor_a)
    print(Calculadora.soma())
    print(Calculadora.subtracao())
    print(Calculadora.divisao())
    print(Calculadora.multiplicacao())


# print(soma(1, 2 ))
# print(soma(4, 4))
# print(subtracao(10, 2))
# print(multiplicacao(15, 3))
# print(divisao(50, 5))