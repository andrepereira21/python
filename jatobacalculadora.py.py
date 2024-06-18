class Calculadora:
    def __init__(self):
        pass
    
    def soma(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y
    
    def multiplicacao(self, x, y):
        return x * y
    
    def divisao(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Erro: divisão por zero!"

# Exemplo de uso
calc = Calculadora()
print("Soma:", calc.soma(5, 3))
print("Subtração:", calc.subtracao(5, 3))
print("Multiplicação:", calc.multiplicacao(5, 3))
print("Divisão:", calc.divisao(5, 3))
print("Divisão por zero:", calc.divisao(5, 0))
